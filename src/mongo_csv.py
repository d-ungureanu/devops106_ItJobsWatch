import pandas as pd
from pymongo import MongoClient
import json



while True:
    try:
        client = MongoClient(port = 27017)
        db = client.it_job_watch
        col = db.it_job_watch_data
        break
    except Exception as e:
        print("Trying to create a connection to the database")
        time.sleep(2)

filepath = 'C://Users/emile/Downloads/ItJobsWatchTop30.csv'

data = pd.read_csv(filepath, encoding = 'unicode_escape')
data_json = json.loads(data.to_json(orient='records'))
col.drop()
col.insert_many(data_json)