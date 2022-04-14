import requests
import os.path
from config_manager import itjobswatch_home_page_test_file, itjobswatch_home_page_url, itjobswatch_perm_search_test_page


class HttpManager:

    def __init__(self, file_or_url_location):
        self.url_response = None
        self.html = None
        self._get_html_file_or_url(file_or_url_location)

    def _get_html_file_or_url(self, file_location_or_url_location):
        if os.path.exists(file_location_or_url_location):
            self.html = open(file_location_or_url_location).read()
        elif 'http' in file_location_or_url_location:
            response = requests.get(file_location_or_url_location)
            self.url_response = response
            self.html = response.content.decode("utf-8")
        else:
            raise NameError("Please ensure your file or url have the correct path")

    def get_response_code(self):
        return self.url_response.status_code


if __name__ == '__main__':
    print(HtmlResponseManager(itjobswatch_home_page_test_file()).html)
