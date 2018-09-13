# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item , Field


class DoubanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    writer = Field()
    publish = Field()
    translator = Field()
    origin_name = Field()
    publish_time = Field()
    page_num = Field()
    price = Field()
    ISBN = Field()
    decorate = Field()
