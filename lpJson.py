from selenium.webdriver.firefox.options import Options as FirefoxOptions
import filesHandler as fh
import lpCrawler as lp


def scrape_charts(filepath):
    """ Scrape the data of all the charts of Polish Radio Program 3. """
    ff_options = FirefoxOptions()
    ff_options.add_argument('--headless')
    driver = lp.LPCrawler(options=ff_options)
    data = driver.get_charts()
    fh.write_json(filepath, data)
    driver.quit()



