# -*- coding: utf-8 -*-
import os

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from doutuwang.items import DoutuwangItem


class DtSpider(CrawlSpider):
    name = 'dt'
    allowed_domains = ['doutula.com']
    start_urls = ['http://www.doutula.com/article/list/?page=1']

    rules = (
        # Rule(LinkExtractor(allow=r'http://www.doutula.com/article/list/?page=.+'), callback='parse_item', follow=True),
        # 页面显示的url
        Rule(LinkExtractor(allow=r'/article/list/\?page=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        category = response.xpath("//div[@class='col-sm-9 center-wrap']/a/div/text()").getall()
        img_url = response.xpath("//div[@class='col-sm-9 center-wrap']//img/@data-original").getall()
        # img_url = list(map(lambda x: x.replace("//static.doutula.com/img/gif.png?33", " "), img_url))
        yield DoutuwangItem(category=category, image_urls=img_url)
    # def parse(self, response):
    #     print("我进parse了")
