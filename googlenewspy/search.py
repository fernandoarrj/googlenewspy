import requests

from .exceptions import SearchGoogleNewsError
from .parse import ParseSearch


class Search:
    def __init__(self, host_language='pt-BR', geolocation='BR'):
        """
            The user can set host language and geolocation
            for better search results.
        """
        self.geolocation = geolocation
        self.host_language = host_language
        self.url_base = 'https://news.google.com'

    def get(self, url):
        """Make the request of some url google news"""
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
        msg = f'Something went wrong status code is {resp.status_code}'
        raise SearchGoogleNewsError(msg)

    def news(self, text):
        """Get news with some text"""
        url = (f'{self.url_base}/search?q={text}'
              f'&hl={self.host_language}&gl=${self.geolocation}')

        html = self.get(url)
        parsed_data = ParseSearch().handle(html)
        return parsed_data
