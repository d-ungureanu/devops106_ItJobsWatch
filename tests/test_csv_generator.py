from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30
from config_manager import itjobswatch_home_page_url, itjobswatch_home_page_test_file, get_test_env_setting
from definitions import TEST_RESOURCES_FOLDER
import pytest
import csv
import os


class TestCSVGenerator:

    # The below fixture sets up whether you are testing locally on stubs or against live HTTP calls
    # This is defined in the config.ini file in the root of this project
    @pytest.fixture(scope='module')
    def generate_top_30_html_object(self):
        if get_test_env_setting() == 'live':
            return ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
        else:
            return ItJobsWatchHomePageTop30(itjobswatch_home_page_test_file())

    # the below fixtures relate to the setup and teardown for testing csv generation based on giving the
    # top 30 CSV Generator a defined path
    @pytest.fixture(scope='module', autouse=True)
    def create_top_30_test_csv(self, generate_top_30_html_object):
        csv_generator_object = Top30CSVGenerator()
        csv_generator_object.generate_top_30_csv(generate_top_30_html_object.get_top_30_table_elements_into_array(), TEST_RESOURCES_FOLDER, '/top_30_without_headers.csv')
        yield self.create_top_30_test_csv
        os.remove(TEST_RESOURCES_FOLDER + '/top_30_without_headers.csv')

    @pytest.fixture(scope='module', autouse=True)
    def create_top_30_test_csv_with_headers_with_specified_location(self, generate_top_30_html_object):
        csv_generator_object = Top30CSVGenerator()
        csv_generator_object.generate_top_30_csv(generate_top_30_html_object.get_top_30_table_elements_into_array(), TEST_RESOURCES_FOLDER, '/top_30_with_headers.csv', 'yes')
        yield self.create_top_30_test_csv_with_headers_with_specified_location
        os.remove(TEST_RESOURCES_FOLDER + '/top_30_with_headers.csv')

    @pytest.fixture(scope='module', autouse=True)
    def create_top_30_using_default_location_and_default_name(self, generate_top_30_html_object):
        csv_generator_object = Top30CSVGenerator()
        csv_generator_object.generate_top_30_csv(generate_top_30_html_object.get_top_30_table_elements_into_array())
        yield self.create_top_30_using_default_location_and_default_name
        os.remove(os.path.expanduser('~/Downloads/') + 'ItJobsWatchTop30.csv')

    # testing csv generation based on giving the top 30 CSV Generator a defined path
    def test_csv_without_headers(self):
        list_count = 0
        with open(TEST_RESOURCES_FOLDER + '/top_30_without_headers.csv') as top_30_without_headers:
            parsed_csv_file = csv.reader(top_30_without_headers)
            for line in parsed_csv_file:
                list_count += 1

        assert list_count == 30

    def test_csv_with_headers(self):
        list_count = 0
        with open(TEST_RESOURCES_FOLDER + '/top_30_with_headers.csv') as top_30_without_headers:
            parsed_csv_file = csv.reader(top_30_without_headers)
            for line in parsed_csv_file:
                list_count += 1

        assert list_count == 31

    def test_csv_without_headers_default_location(self):
        list_count = 0
        with open(os.path.expanduser('~/Downloads/') + 'ItJobsWatchTop30.csv') as top_30_without_headers:
            parsed_csv_file = csv.reader(top_30_without_headers)
            for line in parsed_csv_file:
                list_count += 1

        assert list_count == 30