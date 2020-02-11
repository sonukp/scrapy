import scrapy

class QuoteSpider(scrapy.Spider):
    #name and start_url is is aspected by scrapy so these are not changed
    name = 'quote'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self,response):
        #response contains all the source code of the website
        title = response.css('title::text').extract()
        yield {'titletext': title}   #use with generators and generators being used by the scrapy
