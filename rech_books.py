import config

client = config.client
db = config.db

class Search(object):
 
  def __init__(self):
    pass
  
  @staticmethod
  def rech_classique(search_query):
        result = db["books"].find({
            "$or":[
                {"type":{"$regex":search_query,"$options":"i"}},
                {"title":{"$regex":search_query,"$options":"i"}},
                {"year":{"$eq":search_query}},
                {"booktitle":{"$regex":search_query,"$options":"i"}},
                {"authors":{"$regex":search_query,"$options":"i"}},
            ]}).limit(10)
        return result

  @staticmethod
  def filter_type(input_type):
        result_1 = db["books"].find({"type":{"$regex":input_type,"$options":"i"}} ).limit(10)
        return result_1

  @staticmethod
  def filter_title(input_title):
            result_2 = db["books"].find({"title":{"$regex":input_title,"$options":"i"}}).limit(10)
            return result_2

  @staticmethod
  def filter_year(input_year):
            result_3 = db["books"].find({"year":{"$eq":input_year}}).limit(10)
            return result_3

  @staticmethod
  def filter_booktitle(input_cat):
            result_4 = db["books"].find({"booktitle":{"$regex":input_cat,"$options":"i"}}).limit(10)
            return result_4

  @staticmethod
  def filter_authors(input_author):
            result_5 = db["books"].find({"authors":{"$regex":input_author,"$options":"i"}}).limit(10)
            return result_5

  # fonction Count générique
  # @staticmethod
  # def count_docs(input_exist):
  #        result_exist = db["books"].count_documents({
  #           "$or":[
  #               {"type":{"$regex":input_exist,"$options":"i"}},
  #               {"title":{"$regex":input_exist,"$options":"i"}},
  #               {"year":{"$eq":input_exist}},
  #               {"booktitle":{"$regex":input_exist,"$options":"i"}},
  #               {"authors":{"$regex":input_exist,"$options":"i"}},
  #           ]})
  #        return result_exist