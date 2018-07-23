# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones/']

    def parse(self, response):
        titles = response.css('h2.joZVyL::text').extract()
        votes  = response.css('.scrollerItem>div>div>div::text').extract()
        time = response.css("a[data-click-id=timestamp]::text").extract()
        print(titles)
        print(votes)
        print(time)
        for item in zip(titles, votes, time):
            scraped_info = {
                    'title':item[0],
                    'vote':item[1],
                    'created_at':item[2],
                    }
            yield scraped_info

                
