# -*- coding: utf-8 -*-
import scrapy
import json


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/']

    def start_requests(self):
        '''
        人人网登录操作
        使用 yield 与 scrapy 的 FormRequest 提交用户登录信息，并使用回调方法访问 parse 来接下来处理返回的代码。
        
        注意：测试时请使用您的用户名与密码
        
        '''

        # 登录页面的 URL
        login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018821943682'

        # 登录的表单信息，其中用户名与密码请自行输入正确值
        data = {
        	'email': '15899962740',
            'icode': '',
            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id': '1',
            'captcha_type': 'web_login',
            'password': '636e86c68d31cee6fed50e4b11f30e34c47cdbdee9a150f67e1aa201fcd18ff6',
            'rkey': '9f7775264b4cfba8c894b2e947e3a60c',
            'f': 'http%3A%2F%2Fwww.renren.com%2F330188649%2Fprofile',
        }
        
        yield scrapy.FormRequest(
            url = login_url,
            formdata = data,
            callback = self.parse
        )

    def parse(self, response):
        '''
        爬虫 start_requests 方法的回调函数。
        返回的是 JSON 数据，解析 response 将数据取出，如果登录失败，显示其中的 failDescription 值。
        如果这个字段不存在，则说明登录成功打印登录成功。

        '''
        res = json.loads(response.text)

        print('='*64)
        if(res['failDescription']):
            print("登录失败，原因是："+res['failDescription'])
        else:
            print("登录成功")
            #print(response.selector.css("a.hd-name::text").extract())

        print('='*64)