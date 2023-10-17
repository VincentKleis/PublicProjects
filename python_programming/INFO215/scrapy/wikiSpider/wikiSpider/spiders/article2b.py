import scrapy
from wikiSpider.items import Article

class ArticleSpider(scrapy.Spider):
    name='article2b'
    allowed_domains = ['en.wikipedia.org']

    start_urls = ['http://en.wikipedia.org/wiki/Python_%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python']

    def parse(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.xpath('//h1/text()').extract_first()
        lastUpdated = response.xpath("//*[@id='footer-info-lastmod']/text()").extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
        yield article

        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)

