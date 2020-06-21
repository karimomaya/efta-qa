from excel import generate_excel
from mongodb import connect_to_db, get_collection


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
    db = connect_to_db()
    collection = get_collection(db, "content")
    docs = collection.aggregate(init_pip())
    generate_excel('data', docs)
    print(docs)


if __name__ == '__main__':
    export_excel()
