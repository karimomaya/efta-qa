from pymongo import MongoClient
import json



with open('config.json') as json_data_file:
    config = json.load(json_data_file)


def connect_to_db():
    connection = MongoClient(config['mongo']['host'], config['mongo']['port'], unicode_decode_error_handler='ignore')
    db = connection[config['mongo']['database']]
    db.authenticate(config['mongo']['user'], config['mongo']['passwd'], 'admin')
    return db


def get_collection(db, collection):
    return db[collection]
