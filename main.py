from pymongo import MongoClient
import json
from excel import generate_excel

with open('config.json') as json_data_file:
    config = json.load(json_data_file)


def connect_to_db():
    connection = MongoClient(config['mongo']['host'], config['mongo']['port'], unicode_decode_error_handler='ignore')
    db = connection[config['mongo']['database']]
    db.authenticate(config['mongo']['user'], config['mongo']['passwd'], 'admin')
    return db


def get_collection(db, collection):
    return db[collection]


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


if __name__ == '__main__':
    db = connect_to_db()
    collection = get_collection(db, "content")
    docs = collection.aggregate(init_pip())
    generate_excel('data', docs)
    print(docs)
