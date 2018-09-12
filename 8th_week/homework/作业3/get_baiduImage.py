"""

"""

import urllib.request import urlencode, urlretrieve
import requests
import os, time

url = "http://image.baidu.com"

# app.setData('imgData', {})

"""
https://image.baidu.com/search/acjson?
tn=resultjson_com&
ipn=rj&
ct=201326592&is=&
fp=result&
queryWord=%E8%A1%97%E6%8B%8D&
cl=2&
lm=-1&
ie=utf-8&
oe=utf-8&
adpicid=&
st=-1&
z=&
ic=0&
word=%E8%A1%97%E6%8B%8D&
s=&
se=&
tab=&
width=&
height=&
face=0&
istype=2&
qc=&
nc=1&
fr=&
expermode=&
pn=30&
rn=30&
gsm=1e&
1536761112628=

"""


def getPage(offset):

    data = {
        'tn'        : 'resultjson_com',
        'ipn'       : 'rj',
        'ct'        : '201326592',
        'is'        : '',
        'fp'        : 'result',
        'queryWord' : '街拍',
        'cl'        : '2',
        'lm'        : '-1',
        'ie'        : 'utf-8',
        'oe'        : 'utf-8',
        'adpicid'   : '',
        'st'        : '-1',
        'z'         : '',
        'ic'        : '0',
        'word'      : '街拍',
        's'         : '',
        'se'        : '',
        'tab'       : '',
        'width'     : '',
        'height'    : '',
        'face'      : '0',
        'istype'    : '2',
        'qc'        : '',
        'nc'        : '1',
        'fr'        : '',
        'expermode' : '',
        'pn'        : offset,
        'rn'        : '30',
        'gsm'       : '1e',
        '1536761112628' : '',
    }

    url = "https://image.baidu.com/search/acjson?" + urlencode(data)



def getImage(content):
    pass


def storeImage(item):
    pass


def main():
    pass



if __name__ == '__main__':
    main()
