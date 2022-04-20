from bs4 import BeautifulSoup
from src.http_management.http_manager import HttpManager
from config_manager import itjobswatch_contract_search_test_page
import re




class PermRatesJobSearch:

    def __init__(self, file_or_url_address):
        self._html_manager = HttpManager(file_or_url_address)
        self.job_search = BeautifulSoup(self._html_manager.html, 'html.parser')
        self._validate_search_returns_a_role()

    def _validate_search_returns_a_role(self):
        page_check = self.job_search.find("td", {'class', re.compile("navContainer")}).find('h1', id='h1')
        if page_check is None:
            raise ValueError('Your role type led to a search try using something more specific')


    # Parse perm rates table
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

    def get_rank(self):
        return self.summary_table_data_selector("Rank")

    def get_rank_change_year_on_year(self):
        return self.summary_table_data_selector("Rank change year-on-year")

    def get_percentage_of_jobs_in_uk(self):
        return self.summary_table_data_selector("As % of all permanent jobs advertised in the UK")

    def get_number_of_salaries_quoted(self):
        return self.summary_table_data_selector("Number of salaries quoted")

    def get_median_salary_excluding_london(self):
        return self.summary_table_data_selector("UK excluding London median annual salary")

    def get_permanent_salary_data(self):
        return {"headers": self.get_summary_headers(),
                "Rank": self.get_rank(),
                "Rank change year on year": self.get_rank_change_year_on_year(),
                "median_annual_salary_london_exc": self.get_median_salary_excluding_london()
                "Number of salaries quoted": self.get_number_of_salaries_quoted()}
                # "10th_percentile": self.get_salary_10th_percentile(),
                # "90th_percentile": self.get_salary_90th_percentile()


if __name__ == '__main__':
    print(PermRatesJobSearch("https://www.itjobswatch.co.uk/jobs/uk/sdet.do").summary_table())

    print(PermRatesJobSearch("https://www.itjobswatch.co.uk/jobs/uk/sdet.do").get_permanent_salary_data())

