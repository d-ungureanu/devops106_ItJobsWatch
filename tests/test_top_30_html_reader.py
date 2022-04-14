import pytest
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30
from config_manager import itjobswatch_home_page_url, itjobswatch_home_page_test_file, get_test_env_setting

# Tests in this section are thin as we do not have access to the backend to validate
# They do test that there is no change in expected table size and numbers
class TestTop30HtmlReader():
    @pytest.fixture()
    def top_30_object(self):
        if get_test_env_setting() == 'live':
            return ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
        else:
            return ItJobsWatchHomePageTop30(itjobswatch_home_page_test_file())

    def test_table_with_class_of_results_exists(self, top_30_object):
        assert top_30_object.home_page_html.find('table', {'class': 'results'}).attrs == {'class': ['results']}

    def test_table_headers_are_returned(self, top_30_object):
        assert len(top_30_object.get_table_headers_array()) == 7

    def test_30_objects_returned_from_table_parser(self, top_30_object):
        assert len(top_30_object.get_top_30_table_elements_into_array()) == 30
