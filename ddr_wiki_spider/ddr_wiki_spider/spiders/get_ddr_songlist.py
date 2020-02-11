import scrapy


class DDRSpider(scrapy.Spider):
    name = "ddr"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_Dance_Dance_Revolution_songs'
    ]

    def parse(self, response):
        table = response.xpath("//*[@class='wikitable sortable']//tbody")
        rows = table.xpath('//tr')

        for row in range(1,len(rows)-13):
            yield {
                'song': rows[row].xpath('td//text()')[0].get(),
                'artist': rows[row].xpath('td//text()')[1].get()
            }