import pymongo
from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client["Bibliotheque"]

class Delete(object):

    def __init__(self):
        pass
   
    @staticmethod
    def Supp_classique(input_delete):

        delete_book = db["books"].delete_one({
                "$or":[
                {"type":input_delete},
                {"title":input_delete},
                {"year":input_delete},
                {"booktitle":input_delete},
                {"authors":input_delete},
        ]})
        return delete_book

    @staticmethod
    def supp_type(input_del_type):
        del_type = db["books"].delete_one({"type":input_del_type})
        return del_type
    
    @staticmethod
    def supp_title(input_del_title):
        del_title = db["books"].delete_one({"title":input_del_title})
        return del_title
    
    @staticmethod
    def supp_year(input_del_year):
        del_year = db["books"].delete_one({"year":input_del_year})
        return del_year
    
    @staticmethod
    def supp_cat(input_del_cat):
        del_cat = db["books"].delete_one({"booktitle":input_del_cat})
        return del_cat

    @staticmethod
    def supp_auteur(input_del_auteur):
        del_auteur = db["books"].delete_one({"authors":input_del_auteur})
        return del_auteur