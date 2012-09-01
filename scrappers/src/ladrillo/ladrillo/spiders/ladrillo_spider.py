# coding: utf-8
from redorblue.redblue_spider import RedBlueSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from redorblue.redblue_items import RedBlueItem
from scrapy.http import Request


class LadrilloSpider(RedBlueSpider):
    name = "ladrillo"
    allowed_domains = ["adiosladrilloadios.libremercado.com"]
    start_urls = [
        "http://adiosladrilloadios.libremercado.com/"
    ]
    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths=("//a[@rel='bookmark']", )), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths=("//span[@class='nav-next']", )), callback='parse_page', follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths=("//span[@class='nav-previous']", )), callback='parse_page', follow=True)
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
        item['title'] = self.clean_html(hxs.select("//h1[@class='entry-title']/text()").extract()[0])
        item['clean_text'] = self.clean_html(hxs.select("//div[@class='entry-content article']").extract()[0])

        return item
