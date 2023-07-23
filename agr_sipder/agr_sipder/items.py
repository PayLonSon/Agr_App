# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AgrProdSipderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TransDate = scrapy.Field()
    CropCode = scrapy.Field()
    CropName = scrapy.Field()
    MarketCode = scrapy.Field()
    MarketName = scrapy.Field()
    Upper_Price = scrapy.Field()
    Middle_Price = scrapy.Field()
    Lower_Price = scrapy.Field()
    Avg_Price = scrapy.Field()
    Trans_Quantity = scrapy.Field()
    As_Of_Date = scrapy.Field()
    Pipline = scrapy.Field()

class PxApiSipderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CropName = scrapy.Field()
    Avg_Price = scrapy.Field()
    Suggest_Price = scrapy.Field()
    As_Of_Date = scrapy.Field()
    Pipline = scrapy.Field()
