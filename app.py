import re
from flask import Flask,render_template, request
from requests import post
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30
from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
from config_manager import itjobswatch_home_page_url
from categoryurls import dict_category
from contract_rates_job_search import ContractRatesJobSearch

app = Flask(__name__)

@app.route('/',  methods=["GET", "POST"])
def home():

    if request.method == "POST":
            ### receive element name from HTML ###
            data = request.form.to_dict(flat=False)
            single = (list(data.keys()))
            name = single[0]

            ### check name against url in dict_category and return bs4 of selected url in for rendered table ###
            x = dict_category.get(name)
            site = ItJobsWatchHomePageTop30(x)
            results = site.get_top_30_table_elements_into_array()
            return render_template('index.html', results = results)
           
    else:
        ### Home page will show standard top 30 in GET request ###
        results = ItJobsWatchHomePageTop30(itjobswatch_home_page_url()).get_top_30_table_elements_into_array()
        return render_template('index.html', results = results)


@app.route('/cont',  methods=["GET", "POST"])
def contract_page():

    if request.method == "POST":
        category = request.form["category"]

        beautifyurl = f"https://www.itjobswatch.co.uk/contracts/uk/{category}.do"


        try:
            data = ContractRatesJobSearch(beautifyurl).summary_table()
        
            listres = []
        
            for elements in data.find_all('tr'):
                job = []
                for job_row_items in elements.find_all('td'):
                    job.append(job_row_items.text)
                listres.append(job)

            listres.pop(0)
            listres.pop(0)
            results = listres
        
            return render_template('cont.html', results = results)
        
        except Exception as ex:
            return render_template('apology.html')

    else:
        return render_template('cont.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
