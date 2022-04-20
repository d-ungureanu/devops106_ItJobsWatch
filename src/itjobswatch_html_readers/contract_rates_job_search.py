from bs4 import BeautifulSoup
from src.http_management.http_manager import HttpManager
from config_manager import itjobswatch_contract_search_test_page

import re



class ContractRatesJobSearch:

    def __init__(self, file_or_url_address):
        self._html_manager = HttpManager(file_or_url_address)
        self.job_search = BeautifulSoup(self._html_manager.html, 'html.parser')
        self._validate_search_returns_a_role()

        # html = '<span class="woj"><sup class="versenum">16</sup>The text I want</span>'
        #
        # parsed_element = bs.BeautifulSoup(html, 'html.parser')
        # [s.extract() for s in parsed_element('sup')]
        # text = parsed_element.text

    def _validate_search_returns_a_role(self):
        page_check = self.job_search.find("td", {'class', re.compile("navContainer")}).find('h1', id='h1')
        if page_check is None:
            raise ValueError('Your role type led to a search try using something more specific')

    def summary_table(self):
        return self.job_search.find("table", {'class': re.compile("summary")})

    def get_summary_headers(self):
        summary_headers = []

        for item in self.summary_table().find_all('th', {'class': "hdrCol"}):
            summary_headers.append(item.text)

        return summary_headers

    # [s.extract() for s in parsed_element('sup')]
    # text = parsed_element.tex


    # def summary_table_data_selector(self, table_item_name):
    #     captured_data = []
    #
    #     data_selected = self.summary_table().find('td', text=table_item_name).parent
    #     for item in data_selected.find_all('td', {'class': "fig"}):
    #         captured_data.append(item.text)
    #
    #     return captured_data

    def summary_table_data_selector(self, table_item_name):
        captured_data = []

        data_selected = self.summary_table().find('td', text=table_item_name).parent('sup')
        for item in data_selected.find_all('td', {'class': "fig"}):
            captured_data.append(item.text)

        return captured_data

    def get_rank(self):
        return self.summary_table_data_selector("Rank")

    def get_rank_change_year_on_year(self):
        return self.summary_table_data_selector("Rank change year-on-year")

    def get_percentage_of_jobs_in_uk(self):
        return self.summary_table_data_selector("As % of all permanent jobs advertised in the UK")

    def get_permanent_jobs_citing_name(self, name):
        return self.summary_table_data_selector(f"Permanent jobs citing {name}")

    def get_median_annual_salary(self):
        return self.summary_table_data_selector("Median annual salary (50th Percentile)")

    def get_number_of_salaries_quoted(self):
        return self.summary_table_data_selector("Number of salaries quoted")

    def get_median_day_rate_excluding_london(self):
        return self.summary_table_data_selector("UK excluding London median daily rate")

    def get_day_rate_90th_percentile(self):
        return self.summary_table_data_selector("90th Percentile")

    def get_day_rate_10th_percentile(self):
        return self.summary_table_data_selector("10th Percentile")

    def get_day_rate_data(self):
        return {"headers": self.get_summary_headers(),
                "median_day_rate": self.get_median_annual_salary(),
                "median_day_rate_London_exc": self.get_median_day_rate_excluding_london(),
                "10th_percentile": self.get_day_rate_10th_percentile(),
                "90th_percentile": self.get_day_rate_90th_percentile()}

    def remove_sup(self):

        x = self.summary_table()

        for element in x.find_all('sup'):

            element.extract()

        return x

if __name__ == '__main__':

    print(ContractRatesJobSearch("https://www.itjobswatch.co.uk/contracts/uk/sdet.do").summary_table())
    print(ContractRatesJobSearch("https://www.itjobswatch.co.uk/contracts/uk/sdet.do").get_day_rate_90th_percentile())



