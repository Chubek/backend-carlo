import pymongo
from dotenv import dotenv_values
import random
import os

def random_str(len=5): 
    random_string = ''
 
    for _ in range(len):
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        random_string += (chr(random_integer))

    return random_string


temp = dotenv_values(".env")


client = pymongo.MongoClient(temp["MONGO_URI"])

db = client[temp["MONGO_DB"]]
coll = client[temp["MONGO_COLL"]]

def get_results_from_db(id, job_id):
    return coll.find_one({"id": id, "job_id": job_id})

def insert_results_in_db(id, project_id, save_path):
    job_id = random_str()
    coll.insert_one({"id": id, "project_id": project_id, "job_id": job_id, save_path: save_path})

    return job_id