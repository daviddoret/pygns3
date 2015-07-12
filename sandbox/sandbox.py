__author__ = 'doretd'

import requests

import sysroot

sysroot.log.debug('Hello')

url = 'http://localhost:8000/v1/'

sub_url = 'version'


r = requests.get(url + sub_url)
sysroot.log.debug(r.status_code)
sysroot.log.debug(r.headers['content-type'])
sysroot.log.debug(r.encoding)
sysroot.log.debug(r.text)
sysroot.log.debug(r.json())

###
