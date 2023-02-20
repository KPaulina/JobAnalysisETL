from consts import MANGODB_CONNECTION, DATE
from pymongo import MongoClient
import pandas as pd

#mongodb connection
client = MongoClient(MANGODB_CONNECTION)
db = client.jobs
collection = db.nofluffjobs


def connect_to_mongodb_for_python_jobs():
    list_of_python_jobs = []
    all_python_offers = collection.find({'programming_language': 'Python', 'date': f'{DATE}'})
    for job in all_python_offers:
        list_of_python_jobs.append(job)
    df_python_all_for_the_day = pd.DataFrame(list_of_python_jobs)
    print(df_python_all_for_the_day.info())
    return df_python_all_for_the_day


def connect_to_mongodb_for_new_python_jobs():
    new_python_jobs = []
    new_python_offers = collection.find({'programming_language': 'Python', 'is_new': 'NOWA', 'date': f'{DATE}'})
    for new_job in new_python_offers:
        new_python_jobs.append(new_job)
    df_python_new_jobs = pd.DataFrame(new_python_jobs)
    return df_python_new_jobs
