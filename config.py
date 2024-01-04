import pymongo
from pymongo import MongoClient

# Base de données MongoDB
client = MongoClient("localhost",27017)
db = client["Bibliotheque"]

#test