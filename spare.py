def summary_table_data_selector(self, table_item_name):
        captured_data = []
        data_selected = self.remove_sup().find('td', text=table_item_name)
        for item in data_selected.find_all('td', {'class': "fig"}):
            captured_data.append(item.text)

        print(captured_data)


    def remove_sup(self):
        x = self.summary_table()
        for element in x.find_all('sup'):
            element.extract()
        return x