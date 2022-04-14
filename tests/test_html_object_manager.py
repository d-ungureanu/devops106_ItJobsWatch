import pytest
from config_manager import itjobswatch_home_page_test_file, itjobswatch_home_page_url, get_test_env_setting
from src.http_management.http_manager import HtmlObjectManager


class TestHtmlObjectManager:

    @pytest.fixture()
    def html_manager_object(self):
        if get_test_env_setting() == 'live':
            return HtmlObjectManager(itjobswatch_home_page_url())
        else:
            return HtmlObjectManager(itjobswatch_home_page_test_file())

    def test_html_manager_file_is_opened_correctly(self, html_manager_object):
        assert type(html_manager_object.html) is str

    def test_incorrect_file_or_url_path_raises_name_error(self):
        with pytest.raises(NameError):
            assert HtmlObjectManager("test")

    @pytest.mark.skipif(get_test_env_setting() == 'test', reason='This test is specific to a http call and is not valid when testing locally')
    def test_html_manager_status_response_is_200(self, html_manager_object):
        assert html_manager_object.url_response.status_code == 200

    def test_html_manager_returns_html_from_url(self, html_manager_object):
        assert 'Tracking the IT job market' in html_manager_object.html

