import re


class Regex:
    DATA_CALLBACK = re.compile('AF_initDataCallback[\s\S]*?<\/script')
    DATA_SOURCE_KEY = re.compile('(ds:\d+)')
    DATA_SOURCE_VALUES = re.compile('data:([\s\S]*?), sideChannel: {}}\);<\/')
