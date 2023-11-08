from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikispider.items import Article

class ArticleSpider(CrawlSpider):
    name = 'articles3'

    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.xpath('//h1/text()').extract_first()
        lastUpdated = response.xpath("//*[@id='footer-info-lastmod']/text()").extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
        yield article