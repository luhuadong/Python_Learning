# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem


class PythonbookPySpider(scrapy.Spider):
    name = 'pythonbook.py'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input']

    p = 1 # 爬取页数变量

    def parse(self, response):
        '''
        开始爬取时，调用此方法。首先用xpath拿出所有有效信息，接着在xpath里筛选出对应信息。把对应信息传递给item。
        变量p在这里控制爬取的页数，爬到相应页数就停止。爬取页数内，调用Request方法并用回调函数parse
        :param response: 响应参数
        :return: None
        '''


        dlist = response.selector.xpath(".//ul[@class='bigimg']/li")

        for dd in dlist:
            item = DangdangItem()
            item['name'] = dd.xpath("./a/@title").extract_first() #good
            price = dd.xpath(".//span[@class='search_now_price']").extract_first()
            price = re.findall(".*?([0-9]*\.[0-9]*)",price)
            if(price[0]):
                item['price'] = price[0]
            else:
                item['price'] = None
            item['pic'] = dd.xpath(".//img/@data-original|.//img/@src").extract_first()
            item['author'] = dd.xpath(".//a[@name='itemlist-author']/@title").extract_first()
            item['publisher'] = dd.xpath(".//a[@name='P_cbs']/text()").extract_first() #good
            item['comments'] = dd.xpath(".//a[@class='search_comment_num']/text()").extract_first() #wrong
            item['pubdate'] = dd.re_first("(([0-9]{4})-([0-9]{2})-([0-9]{2}))") #good
            item['description'] = dd.xpath(".//p[@class='detail']/text()").extract_first() # good

            yield item

        self.p += 1

        if(self.p<=10):
            next_url = "http://search.dangdang.com/?key=python&act=input&page_index=" + str(self.p)
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url, callback=self.parse)

