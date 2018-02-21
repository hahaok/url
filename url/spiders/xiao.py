# -*- coding: utf-8 -*-
import scrapy


class XiaoSpider(scrapy.Spider):
    name = 'xiao'

    start_urls = ['http://http://www.qiushu.cc/t/7308/2539752.html/']

    def parse(self, response):
        with open("xiaoshuo.txt",'a') as f:
            f.write(response.css("div ::book_content").extract())
