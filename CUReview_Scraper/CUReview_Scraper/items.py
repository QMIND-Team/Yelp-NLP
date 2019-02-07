# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

#Will define functions to remove html tags and whitespace typical of this approach to webscraping export to csv
#First will define the remove whitespace function so we can pass it into our MapCompose function as a parameter in the input processor
def remove_whitespace(value):
    return value.strip()

#Now define item class Review Item so we can import it into our spider
class ReviewItem(scrapy.Item):
    review_text = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
