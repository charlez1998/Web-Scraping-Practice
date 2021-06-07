import scrapy
from scrapy_selenium import SeleniumRequest

class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'
    
    def start_requests(self):
        yield SeleniumRequest (
            url = "https://slickdeals.net/computer-deals",
            wait_time = 3,
            callback = self.parse, 
        )

    def parse(self, response):
        products = response.xpath('//ul[@class = "dealTiles categoryGridDeals"]/li')
        for product in products:
            yield {
                'name' : product.xpath(".//a[@class = 'itemTitle bp-p-dealLink bp-c-link']/text()").get(),
                'link' : product.xpath(".//a[@class = 'itemTitle bp-p-dealLink bp-c-link']/text()").get(),
                'store_name' : product.xpath("normalize-space(.//span[@class = 'itemStore bp-p-storeLink bp-c-link']/text())").get(),
                'price' : product.xpath("normalize-space(.//div[@class = 'itemPrice  wide ']/text())").get()
            }
