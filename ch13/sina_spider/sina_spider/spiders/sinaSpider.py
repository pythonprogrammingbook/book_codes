# -*- coding: utf-8 -*-
import scrapy

class SinaspiderSpider(scrapy.Spider):
    name = 'sinaSpider'
    allowed_domains = ['www.sina.com.cn']
    start_urls = ['http://www.sina.com.cn/']

    def parse(self, response):
        data_list = []  #用于存储解析到的数据
        #解析HTML源代码，定位新闻内容
        lis = response.xpath("//div[@class='top_newslist']/ul[@class='list-a news_top']//li")
        #将新闻主题和超链接解析出来并整理到列表中
        for li in lis:
            titles = li.xpath(".//a/text()")
            linkes = li.xpath(".//a/@href")
            for title, link in zip(titles, linkes):
                #将新闻主题和对应的超链接组合成字典
                data_dict = {'标题': title.extract(), '链接': link.extract()}
                #将字典数据存储到data_list这个列表中
                data_list.append(data_dict)
        return data_list
