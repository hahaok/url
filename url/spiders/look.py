import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re

class lookSpider(scrapy.Spider):
    name = 'look'
    urls = [
            'https://www.zhihu.com/question/22212644'
    ]


    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, method='GET', callback=self.parse)

    def parse(self, response):
        for stra in response.css('img').xpath('@src').extract():
            if stra.startswith('http'):
                with open('a.txt','a') as f:
                    f.write(stra+'\n')



