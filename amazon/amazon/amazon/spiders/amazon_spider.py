import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1659372229&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        items = AmazonItem()

        product_name = response.css('.a-size-medium::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.s-link-style').css('::text').extract()
        product_price =  1 #response.css('').extract()
        product_image = response.css('.s-image').css('::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image'] = product_image

        yield  items