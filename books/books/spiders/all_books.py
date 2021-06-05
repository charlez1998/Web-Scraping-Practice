import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllBooksSpider(CrawlSpider):
    name = 'all_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = '//article[@class = "product_pod"]/div/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths = '//li[@class = "next"]/a'))
    )

    def parse_item(self, response):
        price = response.xpath('//div[@class="product_price"]/p[1]/text()').get()
        if price:
            price.replace('\u00a3', '')
            
        yield {
            'book_name': response.xpath('//article[@class="product_pod"]/h3/a/text()').get(),
            'price': price,
        }