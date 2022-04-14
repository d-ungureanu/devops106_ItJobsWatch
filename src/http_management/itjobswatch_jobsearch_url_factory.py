from config_manager import itjobswatch_base_contract_url, itjobswatch_base_perm_url

class JobSearchManager:

    def create_job_search_url(self, contract_or_perm, role_to_search_for):
        query = None

        if contract_or_perm.lower() == "contract":
            query = itjobswatch_base_contract_url() + role_to_search_for + '.do'
        elif contract_or_perm.lower() == 'perm':
            query = itjobswatch_base_perm_url() + role_to_search_for + '.do'

        return query.replace(" ", "%20")


if __name__ == '__main__':
    print(JobSearchManager().create_query_string("perm", "qa engineer"))