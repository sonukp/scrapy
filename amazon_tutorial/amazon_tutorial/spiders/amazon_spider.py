# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonTutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    page_number = 2
    start_urls = [
        'https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A20200110-20200209&dc&fst=as%3Aoff&qid=1581244733&rnid=9141481031&ref=sr_hi_2'
    ]

    def parse(self, response):
        items = AmazonTutorialItem()
        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()
        product_image = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image'] = product_image

        yield items

        next_page = 'https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&page=' + str(AmazonSpiderSpider.page_number) + '&fst=as%3Aoff&qid=1581244917&rnid=9141481031&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <= 6:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse())
