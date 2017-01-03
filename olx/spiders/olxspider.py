# -*- coding: utf-8 -*-
import scrapy
import json
import string


class PhoneNumberCrawler(scrapy.Spider):
    name = "phone-number-crawler"
    allowed_domains = ["olx.uz"]
    start_urls = ['http://olx.uz/moda-i-stil/krasota-zdorove/parfyumeriya/']

    def start_requests(self):
        base_url = self.start_urls[0]
        urls = ['{0}?page={1}'.format(base_url, i) for i in range(1, 25)]
        return [scrapy.Request(url=url) for url in urls]

    def parse(self, response):
        selector = scrapy.Selector(response)
        links = selector.xpath('//*[@id="gallerywide"]/li/div/*/a/@href').extract()

        for link in links:
            user_id = link.split('/')[-1].split('#')[0].split('-')[-1].split('.')[0][2:]

            base_url = 'http://olx.uz/ajax/misc/contact/phone/{0}/'
            yield scrapy.Request(url=base_url.format(user_id), callback=self.parse_phone_number)

    def parse_phone_number(self, response):
        if 'value' in response.text:
            obj = json.loads(response.text)
            phone_number = ''.join(filter(lambda x: x.isdigit(), obj['value']))
            return {'number': phone_number}
