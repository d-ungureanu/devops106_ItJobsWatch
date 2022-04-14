from config_manager import itjobswatch_home_page_url
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30
from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
import os

class CmdUserInterface:

    def __init__(self):
        self.menu_options = ['Get ITJobsWatch top 30 - Skills/Roles (csv)']
        self.menu_item_selected = None
        self.menu_control()

    def _generate_menu(self):
        service_menu = "\nPlease select a number from the below menu: \n"
        menu_counter = 1
        for item in self.menu_options:
            service_menu += str(menu_counter) + '. ' + item + '\n'
            menu_counter += 1

        self.number_of_menu_items = menu_counter
        service_menu += '\nPlease select an option or type "exit": \n'

        return service_menu

    def menu_control(self):
        print(self._generate_menu())
        option_selected = input()

        if option_selected.lower() == 'exit':
            exit()
        elif option_selected == '':
            self.menu_control()
        elif int(option_selected) == 0 or int(option_selected) > len(self.menu_options):
            print('Please select an option from the menu or type exit')
            self.menu_control()
        elif int(option_selected) == 1:
            self.manage_get_ITJW_top_30_menu()

    def manage_get_ITJW_top_30_menu(self):
        print('Please select from the below menu options\n')
        print('1. Print top 30 to downloads folder with default name (No Headers)')
        print('2. Print top 30 to downloads folder with default name (with Headers)')
        print('3. Return to Main Menu')
        print('or type exit to quit program\n')
        print('Please select option:\n')
        option_selected = input()


        if option_selected.lower() == 'exit':
            exit()
        elif option_selected == '':
            self.manage_get_ITJW_top_30_menu()
        elif int(option_selected) == 1:
            Top30CSVGenerator().generate_top_30_csv(ItJobsWatchHomePageTop30(itjobswatch_home_page_url()).get_top_30_table_elements_into_array())
            print('Please check your downloads folder')
            self.manage_get_ITJW_top_30_menu()
        elif int(option_selected) == 2:
            top_30 = ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
            Top30CSVGenerator().generate_top_30_csv(top_30.get_top_30_table_elements_into_array(), os.path.expanduser('~/Downloads/'), 'ItJobsWatchTop30.csv', top_30.get_table_headers_array())
        elif int(option_selected) == 3:
            self.menu_control()
        else:
            print('Please select an option from the menu or type exit')
            self.manage_get_ITJW_top_30_menu()




if __name__ == '__main__':
    CmdUserInterface().menu_control()