import scrapy
from datetime import datetime

class GloboNewsSpider(scrapy.Spider):
    name = 'globo_news'
    allowed_domains = ['www.globo.com']
    start_urls = ['http://www.globo.com/']

    def parse(self, response):
        data = datetime.now()
        yield {
            "title": response.xpath("//div[@class='highlight headline']/a/@title").get(),
            "title_url": response.xpath("//div[@class='highlight headline']/a/@href").get(),
            "date": data.strftime(f'{data.day}/{data.month}/{data.year}'),
            "hour": data.strftime(f"{data.hour}:{data.minute}") if data.minute >= 10 else data.strftime(f"{data.hour}:0{data.minute}")
        }
