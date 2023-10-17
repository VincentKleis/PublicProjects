from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article

class ArticleSpider(CrawlSpider):
    name = 'articles4'

    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    rules = [
        Rule(LinkExtractor(allow=r'^(https://en.wikipedia.org/wiki/)((?!:).)*$'),
             callback='parse_items', follow=True, cb_kwargs={'is_article': True}),
        Rule(LinkExtractor(allow=r'.*'),
             callback='parse_items', cb_kwargs={'is_article': False})
    ]

    def parse_items(self, response, is_article):
        if is_article:
            article = Article()
            article['url'] = response.url
            article['title'] = response.xpath('//h1/text()').extract_first()
            lastUpdated = response.xpath("//*[@id='footer-info-lastmod']/text()").extract_first()
            article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
            yield article
        else:
            # Do something with non-article page here !!
            pass
