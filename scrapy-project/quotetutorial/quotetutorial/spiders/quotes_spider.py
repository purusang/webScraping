import scrapy
from ..items import QuotetutorialItem
from scrapy.http import FormRequest

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        # print('-------------------------------', token, '-------------------------')
        return FormRequest.from_response(response, formdata = {
            'csrf_token': token,
            'username': 'puru',
            'password': 'purupuru'
        }, callback = self.start_scraping )

    def start_scraping(self, response):
        # print('-------------------------------------++++++++++++++++++++++++++++++++++++++')
        items = QuotetutorialItem()

        all_divs_quotes = response.css('div.quote')
        for quotes in all_divs_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('a.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items