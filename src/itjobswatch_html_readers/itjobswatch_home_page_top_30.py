from bs4 import BeautifulSoup
from src.http_management.http_manager import HttpManager
from config_manager import itjobswatch_home_page_test_file


class ItJobsWatchHomePageTop30:

    def __init__(self, file_or_url_address):
        self._html_manager = HttpManager(file_or_url_address)
        self.home_page_html = BeautifulSoup(self._html_manager.html, 'html.parser')

    def _get_top_30_table(self):
        return self.home_page_html.find('table', class_="results")

    def _get_top_30_table_headers(self):
        return self.home_page_html.find('tr', class_="resultsHeader")

    def get_table_headers_array(self):
        table_headers_list = []

        for item in self._get_top_30_table_headers().find_all('th'):
            table_headers_list.append(item.text)
        table_headers_list.pop(0)

        return table_headers_list

    def get_top_30_table_elements_into_array(self):
        job_list = []

        for elements in self._get_top_30_table().find_all('tr'):
            job = []
            for job_row_items in elements.find_all('td'):
                if job_row_items.attrs['class'] != ['c1']:
                    job.append(job_row_items.text)
            job_list.append(job)

        job_list.pop(0)
        return job_list



if __name__ == '__main__':
    print(ItJobsWatchHomePageTop30(itjobswatch_home_page_test_file()))

