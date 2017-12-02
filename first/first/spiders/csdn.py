# -*- coding: utf-8 -*-
#爬取csdn博客首页推荐文章的标题、简介、链接
import scrapy
from first.items import FirstItem


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        item=FirstItem()
        item['title']=response.xpath('//h2[@class="csdn-tracking-statistics"]/a/text()').extract()
        #item['detail']=response.xpath('').extract()
        item['link']=response.xpath('//h2[@class="csdn-tracking-statistics"]/a/@href').extract()
        yield item

