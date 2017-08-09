
import scrapy

class EbaySpider(scrapy.Spider):
    # declaring name of spider 'ebay'
    name = 'ebay'
    # declaring  allowed domain
    allowed_domain = ["www.ebay.com"]
    start_urls = ["https://www.ebay.com/sch/Cell-Phones-Smartphones-/9355/i.html"]

    def parse(self, response):
        # declaring selector xpath
        titles = response.xpath('//a[@class="vip"]/text()').extract()
        prices = response.xpath('//span[@class="bold"]/text()').extract()
        for item in zip(titles,prices):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'price': item[1],
            }
            yield scraped_info




