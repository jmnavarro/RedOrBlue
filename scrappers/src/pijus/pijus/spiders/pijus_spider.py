# coding: utf-8
from redorblue.redblue_spider import RedBlueSpider
from redorblue.redblue_items import RedBlueItem
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request


class PijusSpider(RedBlueSpider):
    name = "pijus"
    allowed_domains = ["www.agarzon.net"]
    start_urls = [
        "http://www.agarzon.net/"
    ]
    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths=("//a[@rel='bookmark']", )), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths=("//div[@id='paginate']/a", )), callback='parse_page', follow=True)
    )

    def parse_page(self, response):
        hxs = HtmlXPathSelector(response)
        urls = hxs.select("//a[@rel='bookmark']/@href").extract()
        for u in urls:
            yield Request(u, callback=self.parse_item)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)

        item = RedBlueItem()
        item['url'] = response.url
        item['title'] = self.clean_html(hxs.select("//h2/a[@rel='bookmark']/text()").extract()[0])
        paragraphs = hxs.select("//div[@class='post-item']/div[contains(@class, 'post')]/p/text()").extract()
        item['clean_text'] = self.clean_html(' '.join([str for str in paragraphs[:-1]]))

        return item
