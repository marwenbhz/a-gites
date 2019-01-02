# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AGitesItem(scrapy.Item):
    # define the fields for your item here like:
    TITLE_LOCATION = scrapy.Field()
    TITLE_ANNONCE = scrapy.Field()
    PRICE = scrapy.Field()
    LINK_LOCATION = scrapy.Field()
    LINK_ANNONCE = scrapy.Field()
    LINK_ANNONCES = scrapy.Field()
    OWNER = scrapy.Field()
    DESCRIPTION = scrapy.Field()
    TYPE_LOGEMENT = scrapy.Field()
