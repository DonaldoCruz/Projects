import requests  # This library allows the sending of HTTP requests easily.
from bs4 import BeautifulSoup  # This library allows the extraction of data from HTML/XML files.
from datetime import date, datetime
import time

import pprint  # To make the printing of dictionaries formatted.

__today = date.today()  # Returns a Date object with today's date.
# Returns a string in the form YYYY-MM-DD (e.g., 2021-05-01) with the year being the previous year.
__default_start_date = __today.replace(year=__today.year-1, day=1)
print(__default_start_date)
# Returns a string in the form YYYY-MM-DD. (e.g., 2022-05-01)
__default_end_date = __today.replace(day=1).isoformat()
print(__default_end_date)

# Process: Get Iso format date -> convert to date object -> convert to epoch timestamp
parameters = {
    'period1': __default_start_date,
    'period2': __default_end_date,
    'interval': '1d'  # One day intervals
}
unixtime = int(time.mktime(__default_start_date.timetuple()))  # Converting date object to epoch timestamp
print(unixtime)

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
        """


    # By setting the User-Agent header, it will allow us to bypass the bot protection. Without it, we cannot scrape Yahoo Finance.
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'  # For more info on User-Agent string: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
    }

    __today = date.today()  # Returns a Date object with today's date.
    # Returns a string in the form YYYY-MM-DD (e.g., 2021-05-01) with the year being the previous year.
    __default_start_date = date(year=__today.year - 1, month=__today.month, day=1).isoformat()
    # Returns a string in the form YYYY-MM-DD. (e.g., 2022-05-01)
    __default_end_date = date(year=__today.year, month=__today.month, day=1).isoformat()

    def __init__(self, ticker):
        """
        Parameters
        ----------
        ticker: str
            The ticker symbol of a company (e.g., Tesla's ticker symbol is TSLA).
        """
        self.url = f'https://finance.yahoo.com/quote/{ticker}/history'

    def get_page(self):
        print()
        return requests.get(url=self.url, headers=self.HEADERS)  # Returns a response object containing the desired web page.

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


# obj = CompanyRecon('TSLA')
# res = obj.get_page()
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
# print(res)
# print(res)
