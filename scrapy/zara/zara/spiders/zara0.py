# -*- coding: utf-8 -*-
import scrapy
import logging 
from scrapy.utils.log import configure_logging

class Zara0Spider(scrapy.Spider):
    name = 'zara0'
    allowed_domains = ['www.zara.com']
    start_urls = ['http://www.zara.com/in/en/woman-shirts-l1217.html']
    custom_settings = {
            'FEED_URI':"zara0.csv",
            }
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
        )
    

    def parse(self, response):
        hrefs = response.css("li.product a.item::attr(href)")
        for url in hrefs:
            # scrape = {'href':url,}
            # print("product" + url)
            yield response.follow(url, self.parse_item)
            # yield scrape


    def parse_item(self, response):
        imgs = response.css("._seoImg img::attr(src)").extract()
        alts = response.css("._seoImg img::attr(alt)").extract()
        for img, alt in zip(imgs, alts):
            scraped = {
                    'img_url':img,
                    'description':alt,
                    }
            yield scraped
