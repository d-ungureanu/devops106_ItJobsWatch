from bs4 import BeautifulSoup
from src.http_management.http_manager import HttpManager
from config_manager import itjobswatch_contract_search_test_page

import re

class ContractRatesJobSearch:

    def __init__(self, file_or_url_address):
        self._html_manager = HttpManager(file_or_url_address)
        self.job_search = BeautifulSoup(self._html_manager.html, 'html.parser')
        self._validate_search_returns_a_role()

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

    def summary_table_data_selector(self, table_item_name):
        captured_data = []
        data_selected = self.summary_table().find('td', text=table_item_name).parent
        for item in data_selected.find_all('td', {'class': "fig"}):
            captured_data.append(item.text)

        return captured_data

    def get_median_day_rate(self):
        return self.summary_table_data_selector("UK median daily rate")

    def get_median_day_rate_excluding_london(self):
        return self.summary_table_data_selector("UK excluding London median daily rate")

    def get_day_rate_90th_percentile(self):
        return self.summary_table_data_selector("90th Percentile")

    def get_day_rate_10th_percentile(self):
        return self.summary_table_data_selector("10th Percentile")

    def get_day_rate_data(self):
        return {"headers": self.get_summary_headers(),
                "median_day_rate": self.get_median_day_rate(),
                "median_day_rate_London_exc": self.get_median_day_rate_excluding_london(),
                "10th_percentile": self.get_day_rate_10th_percentile(),
                "90th_percentile": self.get_day_rate_90th_percentile()}

if __name__ == '__main__':

    print(ContractRatesJobSearch(itjobswatch_contract_search_test_page()).get_day_rate_data())


