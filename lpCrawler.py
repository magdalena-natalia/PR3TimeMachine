import time
from selenium import webdriver


class LPCrawler(webdriver.Firefox):
    """ A class to represent a crawler operating on a website with Polish Radio 3 Charts. """

    def load_chart_menu(self):
        """ Load the menu of chart search. """
        charts_menu = self.find_element_by_class_name('search-edition')
        charts_menu.click()

    def load_first_chart(self):
        """ Load the subpage with the first chart. """
        self.load_chart_menu()
        link_to_chart = self.find_element_by_class_name('button')
        link_to_chart.click()

    def load_next_chart(self):
        """ Load the subpage with the next chart. """
        link_to_chart = self.find_element_by_class_name('nav-next')
        link_to_chart.click()

    def find_info(self):
        """ Return the header of the chart including its number, date and host. """
        info_html = self.find_elements_by_css_selector('h1 strong')
        return [element.text for element in info_html]

    @staticmethod
    def find_date(info):
        """ Return the date of the chart. """
        return info[1]

    @staticmethod
    def find_number(info):
        """ Return the formal number of the chart. """
        return info[0]

    @staticmethod
    def find_host(info):
        """ Return the name of the chart host """
        return info[2]

    def find_titles(self):
        """ Return the titles of the chart songs. """
        titles_html = self.find_elements_by_class_name('song_title')
        return [title_html.text for title_html in titles_html]

    def find_artists(self):
        """ Return the performers of the chart songs. """
        artists_html = self.find_elements_by_class_name('song_performer')
        return [artist_html.text.title() for artist_html in artists_html]

    def get_chart(self, chart_id):
        """ Return chart data including its number, date, titles and artists. """
        info = self.find_info()
        data = {
            # 'id': chart_id,
            'id': f'{chart_id}',
            'number': LPCrawler.find_number(info),
            'date': LPCrawler.find_date(info),
            'titles': self.find_titles(),
            'artists': self.find_artists()
        }
        return data

    def get_charts(self):
        """ Return  all charts data including their id-s, numbers, dates, titles and artists. """

        main_url = 'https://www.lp3.pl/'
        # 40 charts less than the website counter shows due to double and triple ones
        number_of_charts = 1958
        charts = []
        data = {'chart': charts}

        self.get(main_url)
        self.load_first_chart()
        for i in range(1, number_of_charts + 1):
            # TODO delete TEST
            # slow down to give JavaScript time to load the entire code of a subpage
            time.sleep(1)
            # print(i)
            chart = self.get_chart(i)
            charts.append(chart)
            self.load_next_chart()
        return data
