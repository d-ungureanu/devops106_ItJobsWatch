import os
import time
from flask import Flask, request, jsonify
from src.itjobswatch_html_readers.perm_rates_job_search import PermRatesJobSearch
import mongo_csv
app = Flask(__name__)

@app.route('/', methods=["GET"])
def home_page():

    return "welcome"

@app.route('/top30', methods=["GET"])
def top_30_page():

    return jsonify(mongo_csv.csv_to_db())

@app.route('/perm_requests/<data>', methods=["GET"])
def perm_req(data):

    if data == "1":
        testing = PermRatesJobSearch("https://www.itjobswatch.co.uk/jobs/uk/agile.do").get_permanent_salary_data()
        test = str(testing)
        print(test)
        return test

@app.route('/job_role_info/<job_title>')
def job_role_info(job_title):

    mongo_csv.trigger_site_scrape()
    return jsonify(mongo_csv.get_job(job_title))


if __name__ == "__main__":

    app.run(port=8080, debug=True)
