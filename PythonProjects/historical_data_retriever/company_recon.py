from datetime import date  # This class is used to work with dates.
from selenium import webdriver  # This class will allow us to navigate to a desired web page.
from selenium.webdriver.common.by import By  # This class is used to find elements on the page.
from selenium.webdriver.chrome.service import Service  # This class along with the ChromeDriverManager class are used to create the webdriver.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait  # This class along with expected_conditions class will be used to locate an element.
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time  # This library is used, so we can convert a date to unix time.
import os


class CompanyRecon:
    """
    A class used to retrieve historical data from a certain company using Yahoo Finance.

    ---

    Instance Variables
    ------------------
    ticker: str
        a string with the value of a company's ticker symbol.
    url: str
        a string representing the URL where we will get the historical stock data of a company (e.g., Tesla's ticker symbol is TSLA).

    Methods
    -------
    get_historical_data(start_date, end_date)
        This method downloads the stock data of a specified company as a csv file.

    datetime_to_unix(date_str)
        This method converts a string representing a date in ISO 8601 format to unix time (Seconds since epoch).
    """


    # By setting the User-Agent header, it will allow us to bypass the bot protection. Without it, we cannot scrape Yahoo Finance.
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'  # For more info on User-Agent string: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
    }

    __today = date.today()  # Returns a Date object with today's date.
    # Returns a string in the form YYYY-MM-DD (e.g., 2021-05-01) with the year being the previous year.
    __default_start_date = __today.replace(year=__today.year-1, day=1).isoformat()
    # Returns a string in the form YYYY-MM-DD. (e.g., 2022-05-01)
    __default_end_date = __today.isoformat()

    def __init__(self, ticker):
        """
        Parameters
        ----------
        ticker: str, required
            The ticker symbol of a company (e.g., Tesla's ticker symbol is TSLA).
        """
        self.__ticker = ticker  # This instance variable is to identify which company we are working with.
        self.__url = f'https://finance.yahoo.com/quote/{ticker}/history'  # This is the url where we will scrape the data from.

    def get_historical_data(self, start_date=__default_start_date, end_date=__default_end_date):
        """
        This method downloads the stock data of the specified company.

        Parameters
        ----------
        start_date: str, required
            a string representing a date in ISO 8601 (YYYY-MM-DD).
        end_date: str, required
            a string representing a date in ISO 8601 (YYYY-MM-DD).

        Returns
        -------
        boolean
            True if the csv file was downloaded.

        Raises
        ------
        Timeout Exception
            when the html element with the download link is not found.

        """
        # Converting the dates to unix time because that's what the parameters must be in order to get the correct page.
        start_date = self.datetime_to_unix(start_date)
        end_date = self.datetime_to_unix(end_date)
        if start_date > end_date:
            print('Start date must be prior to end date.')
            return False

        self.__url += f'?period1={start_date}&period2={end_date}&interval=1d'  # Adding a query string to the url.
        # "options" and "prefs" variables help set the preferences to the Chrome browser.
        options = webdriver.ChromeOptions()
        prefs = {
            'download.default_directory': os.getcwd(),  # downloads the csv file to the directory where this file is in.
        }
        options.add_experimental_option('prefs', prefs)  # This method allows us to add preferences to the webdriver object.
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # Instance of Chrome webdriver is created.
        driver.get(self.__url)  # This will navigate to the historical page on yahoo finance.
        try:
            WebDriverWait(driver, 60).until(  # This waits for the anchor element with the download link to appear, and then clicks it to download the file.
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[download="{self.__ticker}.csv"]'))
            ).click()
            time.sleep(5)  # This helps download the file completely. Without this, the file partially downloads as a TMP file.
        except TimeoutException:
            print('Timed out, could not locate HTML anchor element with the link to download the CSV file. '
                  'Check if the correct ticker symbol was provided.')
            driver.close()
            return False
        else:
            print('CSV File Downloaded')
        driver.close()
        return True

    @staticmethod
    def datetime_to_unix(date_string):
        """
        This method converts a string in ISO 8601 format (YYYY-MM-DD) to unix time.

        Parameters
        ----------
        date_string: str, required
            a string representing a date in ISO 8601 format.

        Returns
        -------
            an integer representing unix time (Seconds since the epoch). returns None if argument passed is invalid.

        Raises
        ------
        TypeError
            when the argument passed is not a string in the format of YYYY-MM-DD.
        """
        unix_time = None
        try:
            date_obj = date.fromisoformat(date_string)  # Generating a data object from an ISO 8601 formatted string.
            unix_time = int(time.mktime(date_obj.timetuple()))  # Converting date object to unix time.
        except (TypeError, ValueError) as error:
            print('Invalid input. Input must be a string in the form: YYYY-MM-DD. (Year-Month-Day)')
        return unix_time


obj = CompanyRecon('AAPL')
res = obj.get_historical_data('2019-02-01', '2020-02-01')
