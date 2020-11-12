# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    

    script = '''
    function main(splash,args)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(3))
        eth_tab = assert(splash:select_all(".filterPanelItem___2z5Gb "))
        eth_tab[4]:mouse_click()
        splash:wait(2)
        splash:set_viewport_full()
        return splash:html()
    end'''

    def start_requests(self):
        yield SplashRequest(url="https://www.livecoin.net/en",callback=self.parse,endpoint="execute",
        args={'lua_source':self.script})




    def parse(self, response):
        for currency in response.xpath("//div[contains(@class,'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield{
                'currency Pair' : currency.xpath('.//div[1]/div/text()').get(),
                'volume(24h)' : currency.xpath('.//div[2]/span/text()').get(),

            }
