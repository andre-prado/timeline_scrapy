import scrapy
from datetime import datetime

class GloboNewsSpider(scrapy.Spider):
    name = 'globo_news'
    allowed_domains = ['www.globo.com']
    start_urls = ['http://www.globo.com/']

    def parse(self, response):
        data = datetime.now()

        title_sdt = response.xpath("normalize-space(//div[@class='highlight headline']/a/@title)").get()
        title_url_sdt = response.xpath("normalize-space(//div[@class='highlight headline']/a/@href)").get()

        title_photo = response.xpath("normalize-space(//div[@class='highlight photo']/a[@class='highlight__link with-picture']/@title)").get()
        title_photo_url = response.xpath("normalize-space(//div[@class='highlight photo']/a[@class='highlight__link with-picture']/@href)").get()


        date = data.strftime(f'{data.day}/{data.month}/{data.year}')
        hour = data.strftime(f"{data.hour}:{data.minute}") if data.minute >= 10 else data.strftime(f"{data.hour}:0{data.minute}")

        if title_sdt:
            yield {
                "title": title_sdt,
                "title_url": title_url_sdt,
                "date": date,
                "hour": hour
        }
        elif title_photo:
            yield {
                "title": title_photo,
                "title_url": title_photo_url,
                "date": date,
                "hour": hour
        }
