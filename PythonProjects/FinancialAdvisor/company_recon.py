import requests  # This library allows the sending of HTTP requests easily.
from bs4 import BeautifulSoup  # This library allows the extraction of data from HTML/XML files.

import pprint  # To make the printing of dictionaries formatted.
pp = pprint.PrettyPrinter(indent=4)
res = requests.get('https://api.github.com/events')  # Returns a Response object.

print(res)
# pp.pprint(dict(res.headers))
