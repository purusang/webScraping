import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes_bak'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/pages/2/'
    ]

    def parse(self, response):
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

        next_page = response.xpath('//*[@class="next"]/a/@href').get()
        absolute_next_page_url = response.urljoin(next_page)

        if absolute_next_page_url is not None:
            yield scrapy.Request(absolute_next_page_url)
        # print("-------------next page------------: ", next_page)
        # if next_page is not None:
        #     print("-------------not none next page------------: ", next_page)
        #     response.follow('http://quotes.toscrape.com' + next_page, callback= self.parse)