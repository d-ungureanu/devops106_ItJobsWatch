from src.http_management.itjobswatch_jobsearch import JobSearch


class MultipleSearchHandler:

    def __init__(self, list_of_roles):
        self.list_of_roles = list_of_roles
        self.combined_data_dictionary = {}
        self.job_search = JobSearch()

    def generate_data(self):
        self._populate_data_for_perm_roles()
        self._populate_data_for_contract_roles()
        return self.combined_data_dictionary

    def _populate_data_for_perm_roles(self):
        for role in self.list_of_roles:
            self.combined_data_dictionary.update({role + "_perm": self.job_search.get_permanent_role_salary_range(role)})

    def _populate_data_for_contract_roles(self):
        for role in self.list_of_roles:
            self.combined_data_dictionary.update({role + "_contract": self.job_search.get_contract_role_day_rate_range(role)})

if __name__ == '__main__':
    print(MultipleSearchHandler(['sdet', 'developer', 'data analyst', 'devops']).generate_data())