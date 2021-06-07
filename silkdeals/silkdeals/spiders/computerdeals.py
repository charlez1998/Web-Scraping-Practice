import scrapy


class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'
    allowed_domains = ['https://slickdeals.net/computer-deals/']
    start_urls = ['http://https://slickdeals.net/computer-deals//']

    def parse(self, response):
        pass
