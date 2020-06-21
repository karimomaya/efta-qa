from pymongo import MongoClient

def connect_to_db(config):
    connection = MongoClient(config['mongo']['host'], config['mongo']['port'], unicode_decode_error_handler='ignore')
    db = connection[config['mongo']['database']]
    db.authenticate(config['mongo']['user'], config['mongo']['passwd'], 'admin')
    return db


def get_collection(db, collection):
    return db[collection]
