
# coding: utf-8

# In[8]:


#Need go first import the libraries we're gonna need for this exercise, will start by importing scrapy

import scrapy
from CUReview_Scraper.items import ReviewItem
from scrapy.loader import ItemLoader

#We now define a class that will do our desired scraping for text using scrapy's built-in "spiders"
#These spiders essentially are a template that provide different functionality from spider to spider
#For our intents and purposes, will be using the vanilla scrapy.Spider flavour

class IndeedSpider(scrapy.Spider):

    #Now we must assign a name to our particular spider that will be outlined by the class definition so we can call it when we want to use it

    name = "Indeed"

    #Now must provide the urls to the websites we wish to scrape data from

    start_urls = [

        'https://ca.indeed.com/cmp/Connect-First-Credit-Union/reviews'

    ]

    #Now need to define a parsing function to do the actual scraping

    def parse(self, response):
        for review in response.xpath("//div[@class='cmp-review-text']"):
            l = ItemLoader(item=ReviewItem(), selector=review )
            l.add_xpath('review_text', "//div[@class='cmp-review-text']/p" )
            yield l.load_item()

        next_page = response.xpath("//li[@class = 'next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback  = self.parse)


