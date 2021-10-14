# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import item


class GuaibenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_data = scrapy.Field()
    type_data = scrapy.Field()
    name_data = scrapy.Field()
    pass
class GuaibenItem2(scrapy.Item):
    book_id = scrapy.Field()
    rules = scrapy.Field()
    zhang_name = scrapy.Field()
    content = scrapy.Field()
    wen_url = scrapy.Field()
    pass