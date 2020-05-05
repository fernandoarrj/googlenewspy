from datetime import datetime
import json

from .exceptions import (
    SearchGoogleNewsDataSourceNotFound, SearchGoogleNewsParseError
)
from .maps import Maps
from .regex import Regex
from .utils import Extract


class ParseSearch:

    def handle(self, html):
        matches = Regex.DATA_CALLBACK.findall(html)

        res = {}

        for match in matches:
            key_match = Regex.DATA_SOURCE_KEY.findall(match)
            value_match = Regex.DATA_SOURCE_VALUES.findall(match)

            if key_match and value_match:
                key = key_match[0]
                value = json.loads(value_match[0])

                res[key] = value

        try:
            data = res['ds:1']
        except KeyError:
            raise SearchGoogleNewsDataSourceNotFound

        news = Extract.find(data, Maps.News.data)

        parsed_data = []
        for new in news:
            try:
                title = Extract.find(new, Maps.News.title)
                resume = Extract.find(new, Maps.News.resume)
                url = Extract.find(new, Maps.News.url)
                timestamp = Extract.find(new, Maps.News.timestamp)
                date = datetime.utcfromtimestamp(timestamp)
                parsed_data.append({'title': title, 'resume': resume,
                                    'url': url, 'date': date})
            except Exception as e:
                print(SearchGoogleNewsParseError(e))

        return parsed_data
