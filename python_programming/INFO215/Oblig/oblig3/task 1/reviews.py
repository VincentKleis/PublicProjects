from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from oblig3_task1.items import VergeReview

class crawlspider(CrawlSpider):
    name = 'reviews'

    allowed_domains = ['theverge.com']
    start_urls = ['https://www.theverge.com/reviews']

    reg_rule = r'^(https:\/\/www.theverge.com)(\/[1-9]*)(\/[^/]*)'
    rules = [Rule(LinkExtractor(allow=reg_rule), callback='parse_items',
        follow=True)]

    def parse_items(self, response):
        review = VergeReview()
        review['url'] = response.url
        review['title'] = response.css('h1::text').extract_first()
        review['author_name'] = response.xpath('//span/a[@class="hover:shadow-underline-inherit"]//text()').extract()
        Authror_domain_link = response.xpath('//span/a[@class="hover:shadow-underline-inherit"]/@href').extract_first()
        review['link_auth_prof'] = 'https://www.theverge.com'+Authror_domain_link

        return review
