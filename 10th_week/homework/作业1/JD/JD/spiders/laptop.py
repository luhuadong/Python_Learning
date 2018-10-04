# -*- coding: utf-8 -*-
import scrapy


class LaptopSpider(scrapy.Spider):
    name = 'laptop'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']

    def parse(self, response):
        pass
