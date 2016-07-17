import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from GooglePlayCrawler.items import GoogleItem

class Spider(CrawlSpider):
    name = "google"
    allowed_domains = ["play.google.com"]
    start_urls = [
        'http://play.google.com/',
        'https://play.google.com/store/apps/details?id=com.viber.voip'
    ]
    rules = [
        Rule(LinkExtractor(allow=("https://play\.google\.com/store/apps/details", )), callback='parse_app',follow=True),
    ]

    def parse_app(self, response):
        if response.url.find('reviewId') != -1:
            return;
        item = GoogleItem()
        item['url'] = response.url
        item['numDownloads'] = response.xpath("//div[@itemprop='numDownloads']").xpath("text()").extract()
        item['fileSize'] = response.xpath("//div[@itemprop='fileSize']").xpath("text()").extract()
        item['datePublished'] = response.xpath("//div[@itemprop='datePublished']").xpath("text()").extract()
        item['softwareVersion'] = response.xpath("//div[@itemprop='softwareVersion']").xpath("text()").extract()
        item['operatingSystems'] = response.xpath("//div[@itemprop='operatingSystems']").xpath("text()").extract()
        item['numReviews'] = response.xpath("//span[@class='reviews-num']").xpath("text()").extract()
        item['score'] = response.xpath("//div[@class='score']").xpath("text()").extract()
        yield item
