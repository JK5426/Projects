# -*- coding: utf-8 -*-
import scrapy
# for convert hmtl string into selector object
from scrapy.selector import Selector
#from scrapy_splash import SplashRequest  ## dont required because we use selenium !!!
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which

class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoin.net/en']

    start_urls = [
        "https://www.livecoin.net/en"
    ]
    
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        #chrome_path = which()

        driver = webdriver.Chrome(executable_path="/home/jitendra/projects/livecoin/livecoin/spiders/chromedriver",options=chrome_options)
        driver.set_window_size(1920,1080)
        driver.get('https://www.livecoin.net/en')

        ETH_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        ETH_tab[3].click()
        self.html = driver.page_source            # by default it is return in the form of string 
        #but for using this we can change it into selector object 
        driver.close()

    
    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class,'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield{
                'currency Pair' : currency.xpath('.//div[1]/div/text()').get(),
                'volume(24h)' : currency.xpath('.//div[2]/span/text()').get(),

            }


