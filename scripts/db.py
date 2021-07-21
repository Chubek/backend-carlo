import pymongo
from dotenv import dotenv_values

temp = dotenv_values(".env")


client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client[temp["MONGO_DB"]]
coll = client[temp["MONGO_COLL"]]

def get_results_from_db(id, project_id):
    return coll.find_one({"id": id, "project_id": project_id})

def set_results_in_db(id, project_id, job_id):
    coll.insert_one({"id": id, "project_id": project_id, "job_id": job_id})