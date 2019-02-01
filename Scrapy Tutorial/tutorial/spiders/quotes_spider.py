
# coding: utf-8

# In[8]:


#Need go first import the libraries we're gonna need for this exercise, will start by importing scrapy 

import scrapy 

#We now define a class that will do our desired scraping for text using scrapy's built-in "spiders"
#These spiders essentially are a template that provide different functionality from spider to spider 
#For our intents and purposes, will be using the vanilla scrapy.Spider flavour

class QuoteSpider(scrapy.Spider):
    
    #Now we must assign a name to our particular spider that will be outlined by the class definition so we can call it when we want to use it
    
    name = "quotes"
    
    #Now must provide the urls to the websites we wish to scrape data from, could make this universal by having a variable hold url data, but for our example there's only 2 pages we're scraping so the extra work really isn't necessary
    def start_requests(self):
    
        urls = [
            
        'https://www.yelp.ca/biz/vancity-credit-union-vancouver-4',
        'https://www.yelp.ca/biz/vancity-credit-union-vancouver-8',
        'https://www.yelp.ca/biz/vancity-vancouver-6',
        'https://www.yelp.ca/biz/vancity-vancouver-5',
        'https://www.yelp.ca/biz/vancity-burnaby-2',
        'https://www.yelp.ca/biz/vancity-credit-union-vancouver-5',
        'https://www.yelp.ca/biz/vancity-savings-credit-union-vancouver-5',
        'https://www.yelp.ca/biz/vancity-burnaby-3',
        'https://www.yelp.ca/biz/vancity-burnaby-4',
        'https://www.yelp.ca/biz/vancity-savings-credit-union-vancouver-4',
        'https://www.yelp.ca/biz/vancity-vancouver-2',
        'https://www.yelp.ca/biz/vancity-richmond',
        'https://www.yelp.ca/biz/vancity-vancouver',
        'https://www.yelp.ca/biz/vancity-surrey',
        'https://www.yelp.ca/biz/vancity-credit-union-vancouver-9',
        'https://www.yelp.ca/biz/vancity-vancouver-3',
        'https://www.yelp.ca/biz/vancity-savings-surrey',
        'https://www.yelp.ca/biz/vancity-coquitlam',
        'https://www.yelp.com/biz/vancity-credit-union-vancouver-4?rh_ident=banking_fee&rh_type=phrase'

        
        ]
    
    #Now must have a loop to actually go and do the scraping 
    
        for url in urls:
        
        #Need to call the scrapy.Request function and pass in url as a url parameter and will have define a callback function
        
            yield scrapy.Request(url = url, callback = self.parse)
        
    #Now need to define a callback function to have the above loop work
    
    def parse (self,response):
        
        #Will go back page number, to do that have to have the function check for the page number in the above urls
        #Will take the last 2 characters and split the url where "/" occurs and use the page number as a function end parameter
        
        page = response.url.split("/")[-2]
        
        #Will have a filename to match the above
        filename = 'Vancity Yelp-%s.html' % page
        
        #Will now write the scraped contents to a html file using the code below
        with open(filename,'wb') as f:
            f.write(response.body)
            
        #Although not necessary, will have a self log to see how it's doing as a means of troubleshooting
        self.log('Saved File %s' % filename)

