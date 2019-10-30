 # -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KompasParserItem(scrapy.Item):
    name = scrapy.Field()
    last_update = scrapy.Field()
    import_zones = scrapy.Field()
    import_countries = scrapy.Field()
    export_zones = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()
    country = scrapy.Field()
    description = scrapy.Field()
    source = scrapy.Field()
    product = scrapy.Field()
    hs_code = scrapy.Field()
    date_and_time = scrapy.Field()
