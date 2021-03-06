import scrapy
from ..items import QulaItem


class NovelsSpider(scrapy.Spider):
    name = 'novels'
    allowed_domains = ['m.qu.la']
    # 爬取小说龙族全部章节
    start_page = 4784664
    end_page = 4784781
    for page in range(start_page, end_page):
        start_urls = [
                'https://m.qu.la/book/87705/{}_1.html'.format(page),
                'https://m.qu.la/book/87705/{}_2.html'.format(page)
        ]

    def parse(self, response):
        novel = QulaItem()
        novel['title'] = response.xpath('//*[@id="container"]/div/div/div[2]/h1/text()').extract_first()
        novel['content'] = response.xpath('//*[@id="content"]/text()').extract()
        yield novel