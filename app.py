<<<<<<< HEAD
from flask import Flask,render_template, request
from requests import post
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30
from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
from config_manager import itjobswatch_home_page_url
from categoryurls import dict_category

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


if __name__ == "__main__":
    app.run()
=======
from flask import Flask, render_template, url_for



app = Flask(__name__)




@app.route('/')

def home():
    
   
    return render_template('tools.html')




if __name__ == "__main__":

    app.run(debug = True)
>>>>>>> bb065e2d8c777653265b0e36b039f6d73e46c77e
