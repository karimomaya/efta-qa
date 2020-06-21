from excel import generate_excel
from mongodb import connect_to_db, get_collection
import json

with open('config.json') as config_file:
    config = json.load(config_file)

with open('map-config.json') as map_config_file:
    map_config = json.load(map_config_file)


def update_classification():
    for item in map_config['maps']:
        query = {"classification": item['from']}
        print(query)
        updates = {"$set": {"classification": item['to'], 'classificationArr': item['to'].split(',')}}
        print(updates)
        # db = connect_to_db(config)
        # collection = get_collection(db, "content")
        # updated = collection.update_many(query, updates)
        # print(updated.modified_count)


def init_pip():
    return [
        {
            '$group': {
                '_id': '$classificationArr',
                'total': {'$sum': 1}
            }
        },
        {'$sort': {'_id': 1}}
    ]


def export_excel():
    db = connect_to_db(config)
    collection = get_collection(db, "content")
    docs = collection.aggregate(init_pip())
    generate_excel('data', docs)
    print(docs)


if __name__ == '__main__':
    # export_excel()
    update_classification()
