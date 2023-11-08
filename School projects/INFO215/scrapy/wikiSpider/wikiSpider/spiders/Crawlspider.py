import scrapy

class Crawlspider(scrapy.Spider):

    def start_requests(self):
        url = 'https://www.theverge.com/reviews'

        return super().start_requests()
