import os
import pandas as pd
from pymongo import MongoClient
import json
import time
from config_manager import itjobswatch_home_page_url
from src.csv_generators import top_30_csv_generator
from src.cmd_user_interface import CmdUserInterface

#scrape data, add to csv file
from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30

with open("db.config") as config_file:
    database_url = config_file.read().strip()

while True:
    try:
        client = MongoClient("localhost:27017")
        break
    except Exception as e:
        print("Trying to create a connection to the database")
        time.sleep(2)

db = client.it_job_watch
col = db.it_job_watch_data

def trigger_site_scrape():
    top_30 = ItJobsWatchHomePageTop30(itjobswatch_home_page_url())

    Top30CSVGenerator().generate_top_30_csv(top_30.get_top_30_table_elements_into_array(),
                                            os.path.expanduser('~/Downloads/'),
                                            'ItJobsWatchTop30.csv',
                                            top_30.get_table_headers_array())

def csv_to_db():

    trigger_site_scrape()

    # connect to the database and add the csv

    filepath = 'C:/Users/emile/Downloads/ItJobsWatchTop30.csv'

    data = pd.read_csv(filepath, encoding='unicode_escape')
    data_json = json.loads(data.to_json(orient='records'))

    col.drop()
    col.insert_many(data_json)

    documents = col.find()
    response_list = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response_list.append(document)
    return response_list

def get_job(job_title):

    job_title = str(job_title)
    job_to_find = col.find_one({"Description" : job_title})
    str_job_to_find = str(job_to_find)
    job = str_job_to_find.find("'D")
    last = str_job_to_find.find("}")

    print(str_job_to_find[job:last])
    return str_job_to_find[job:last]





