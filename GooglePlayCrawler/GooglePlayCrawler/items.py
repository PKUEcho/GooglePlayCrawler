# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoogleItem(scrapy.Item):
    url = scrapy.Field()
    numDownloads = scrapy.Field()
    fileSize = scrapy.Field()
    datePublished = scrapy.Field()
    softwareVersion = scrapy.Field()
    operatingSystems = scrapy.Field()
    numReviews = scrapy.Field()
    score = scrapy.Field()