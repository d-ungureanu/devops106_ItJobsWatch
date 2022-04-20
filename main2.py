from src.itjobswatch_html_readers.contract_rates_job_search import ContractRatesJobSearch
from src.itjobswatch_html_readers.perm_rates_job_search import PermRatesJobSearch
from bs4 import BeautifulSoup

if __name__ == "__main__":

    html = 'https://www.itjobswatch.co.uk/jobs/uk/sdet.do'

    parsed_element = BeautifulSoup(html, 'html.parser')
    [s.extract() for s in parsed_element('sup')]
    text = parsed_element.text

    print(text)