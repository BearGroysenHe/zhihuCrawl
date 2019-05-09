# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/signin?next=%2F']
    cookie = {}

    def start_requests(self):
        return []

    def parse(self, response):
        pass
