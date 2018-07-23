# -*- coding: utf-8 -*-
import scrapy


class Zara0Spider(scrapy.Spider):
    name = 'zara0'
    allowed_domains = ['www.zara.com/in/en/']
    start_urls = ['http://www.zara.com/in/en/woman-shirts-l1217.html']
    custom_settings = {
            'FEED_URI':"zara0.csv",
            }
    

    def parse(self, response):
        hrefs = response.css("li.product a.item::attr(href)").extract()
        print(hrefs)
        for link in href:
            scrape = {'href':link,}
            yield scrape
