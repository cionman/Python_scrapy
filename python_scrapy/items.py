# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 책이름
    book_title  = scrapy.Field()

    book_author = scrapy.Field()

    book_translator = scrapy.Field()

    book_pub_date = scrapy.Field()

    book_isbn = scrapy.Field()

