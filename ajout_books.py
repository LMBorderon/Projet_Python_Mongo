import pymongo
from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client["Bibliotheque"]

class Ajout(object):

    def __init__(self):
        pass

    @staticmethod
    def ajout_book(input_type,input_title,input_year,input_cat,input_authors):
        insert_book = db["books"].insert_one({
            "type":input_type,
            "title":input_title,
            "year":input_year,
            "booktitle":input_cat,
            "authors":input_authors
        })
        return insert_book
