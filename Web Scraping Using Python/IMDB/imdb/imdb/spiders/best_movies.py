# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']
    # start_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']

    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url="https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc", headers={
            "user-agent": self.user_agent
            })
    rules = (
        Rule(LinkExtractor(restrict_xpaths=(
            "//h3[@class='lister-item-header']/a")), callback='parse_item', follow=True,process_request="set_user_agent"),
        Rule(LinkExtractor(
            restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), follow=True)
    )
    def set_user_agent(self,request):
        request.headers['user_agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            "title": response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            "year": response.xpath("//span[@id='titleYear']/a/text()").get(),
            "duration": response.xpath("normalize-space((//time)[1]/text())").get(),
            "genre": response.xpath("(//div[@class='subtext']/a)[1]/text()").get(),
            "rating": response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            "moives_url": response.url,
            "user-agent": response.request.headers['User_agent']
        }
