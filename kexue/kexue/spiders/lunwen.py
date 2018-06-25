# -*- coding: utf-8 -*-
import scrapy


class LunwenSpider(scrapy.Spider):
    name = 'lunwen'
    allowed_domains = ['paper.sciencenet.cn']
    start_urls = ['http://paper.sciencenet.cn/paper/fieldlist.aspx?id=2']

    def parse(self, response):
        result = response.xpath('//input[@name="__VIEWSTATE"]/@value').extract()
        myFormData = {
            '__VIEWSTATE' : result,
            '__EVENTTARGET' :  'AspNetPager1',
            '__EVENTARGUMENT'  : '3',
            'AspNetPager1_input' : '2'}
        yield scrapy.FormRequest(url='http://paper.sciencenet.cn/paper/fieldlist.aspx?id=2', formdata=myFormData, method = 'POST', dont_filter = True, callback=self.parse2)


    def parse2(self,response):
        print(response.text)