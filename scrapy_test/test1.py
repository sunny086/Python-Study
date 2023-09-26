import scrapy


class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://blog.csdn.net/babyfish13/article/details/52981110']

    def parse(self, response):
        # 解析网页内容
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('span small.author::text').get()
            yield {'text': text, 'author': author}

        # 继续爬取下一页
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
