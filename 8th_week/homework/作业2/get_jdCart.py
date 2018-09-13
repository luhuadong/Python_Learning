"""
  爬取京东商城网址购物车中的所有商品信息

  采用浏览器伪装技术获取京东购物车信息（维持Cookie信息）

  https://cart.jd.com/cart.action
"""

import requests
import re


def getPage(url):

    res = requests.get(url)

    if res.status_code == 200:
        html = res.content.decode('utf-8')
        return html
    else:
        return None


def parsePage(content):
    pat = '李宁'
    #pat = '<title>(.*?)</title>'
    items = re.findall(pat, content)
    for item in items:
        print(item)


def storeData(content):
    pass


def main():
    url = 'https://cart.jd.com/cart.action'
    content = getPage(url)
    parsePage(content)


if __name__ == '__main__':
    main()
