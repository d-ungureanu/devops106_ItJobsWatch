from src.http_management.itjobswatch_jobsearch_url_factory import JobSearchManager
from src.itjobswatch_html_readers.perm_rates_job_search import PermRatesJobSearch
from src.itjobswatch_html_readers.contract_rates_job_search import ContractRatesJobSearch


class JobSearch(JobSearchManager):

    def get_permanent_role_salary_range(self, role_to_search_for):
        return PermRatesJobSearch(self.create_job_search_url('perm', role_to_search_for)).get_permanent_salary_data()

    def get_contract_role_day_rate_range(self, role_to_search_for):
        return ContractRatesJobSearch(self.create_job_search_url('contract', role_to_search_for)).get_day_rate_data()

if __name__ == '__main__':
    print(JobSearch().get_contract_role_day_rate_range("qa engineer"))