# Google News Py

Search news with python in google news.


## What's necessary
python >=3.6

## Instaling

> pip install googlenewspy

## Using

from googlenewspy import Search\
search = Search()\
text = 'Python'\
search.news(text)

## Features
You can specify witch country and host language in Search object, for better results.
Ex:
> search = Search(host_language='en-US', geolocation='US')\
> search.news('Python')

