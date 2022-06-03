import requests  # This library allows the sending of HTTP requests easily.
from bs4 import BeautifulSoup  # This library allows the extraction of data from HTML/XML files.
from datetime import date, datetime
import time


class CompanyRecon:
    """
    A class used to retrieve historical data from a certain company using Yahoo Finance.

    ---

    Instance Variables
    ------------------
    url: str
        a string representing the URL where we will get the historical stock data of a company (e.g., Tesla's ticker symbol is TSLA).

    Methods
    -------
    get_historical_data(start_date, end_date)
        ************Fill********** BLANK

    get_page()
        This method returns the response after sending a get request to https://finance.yahoo.com/quote/:company_ticker/history endpoint.

    datetime_to_unix(date_str)
        This method converts a string representing a date in ISO 8601 format to unix time (Seconds since epoch).
    """


    # By setting the User-Agent header, it will allow us to bypass the bot protection. Without it, we cannot scrape Yahoo Finance.
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'  # For more info on User-Agent string: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
    }

    __today = date.today()  # Returns a Date object with today's date.
    # Returns a string in the form YYYY-MM-DD (e.g., 2021-05-01) with the year being the previous year.
    __default_start_date = __today.replace(year=__today.year-1, day=1)
    # Returns a string in the form YYYY-MM-DD. (e.g., 2022-05-01)
    __default_end_date = __today.replace(day=1)

    def __init__(self, ticker):
        """
        Parameters
        ----------
        ticker: str, required
            The ticker symbol of a company (e.g., Tesla's ticker symbol is TSLA).
        """
        self.url = f'https://finance.yahoo.com/quote/{ticker}/history'
        print(self.url)

    def get_page(self, start_date, end_date):
        """
        This method returns the response from sending a get request to {url}

        Parameters
        ----------
        start_date: str, required
            a string representing a date in ISO 8601 (YYYY-MM-DD).
        end_date: str, required
            a string representing a date in ISO 8601 (YYYY-MM-DD).

        Returns
        -------
        Response Object
            a response object from get request. (It should be Yahoo Finance page.)
        """
        # Converting the dates to unix time because that's what the parameters must be in order to get the correct page.
        start_date = self.datetime_to_unix(start_date)
        end_date = self.datetime_to_unix(end_date)
        # This dictionary is used to pass data in the URL's query string.
        payload = {
            'period1': start_date,
            'period2': end_date,
            'interval': '1d'  # One day intervals
        }
        try:
            return requests.get(url=self.url, headers=self.HEADERS, params=payload)  # Returns a response object containing the desired web page.
        except (ConnectionError, TimeoutError) as error:
            print('An error occurred while trying to retrieve the response.')

    @staticmethod
    def datetime_to_unix(date_string):
        """
        This method converts a string in ISO 8601 format (YYYY-MM-DD) to unix time.

        Parameters
        ----------
        date_string: required
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
            print(unix_time)
        except (TypeError, ValueError) as error:
            print('Invalid input. Input must be a string in the form: YYYY-MM-DD. (Year-Month-Day)')
        return unix_time

    def get_historical_data(self, start_date=__default_start_date, end_date=__default_end_date):
        """
        This method downloads the historical prices of stocks of a certain company as a csv.

        Parameters
        ----------
        start_date: str, optional
            a string representing a date in ISO 8601 format (YYYY-MM-DD).

        end_date: str, optional
            a string representing a date in ISO 8601 format (YYYY-MM-DD).
        """
        pass


obj = CompanyRecon(54)
res = obj.get_page('2020-01-01', '2021-02-01')
print(type(res))
print(res)

# res = obj.get_page()

# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
# print(res)
# print(res)
