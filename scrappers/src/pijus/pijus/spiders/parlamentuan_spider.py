# coding: utf-8
from scrapy import log
from redorblue.redblue_spider import RedBlueSpider
from redorblue.redblue_items import RedBlueItem
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request


class ParlamentuanSpider(RedBlueSpider):
    name = "parlamentuan"
    allowed_domains = ["parlamentuan.blogspot.com.es"]
    start_urls = [
        "http://parlamentuan.blogspot.com.es/search?updated-max=2012-12-31T15:47:00%2B02:00&max-results=99"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow='parlamentuan.blogspot.com.es/20[0-1][0-9]/[0-9]+/.+..html'), callback='parse_doc', follow=True),
        Rule(SgmlLinkExtractor(allow='parlamentuan.blogspot.com.es/search'), callback='parse_index', follow=True)
    )

    def parse_index(self, response):
        hxs = HtmlXPathSelector(response)
        urls = hxs.select("//h3[contains(@class, 'entry-title')]/a/@href").extract()
        log.msg('Found %i items' % (len(urls),))
        for u in urls:
            log.msg('Enqueue %s' % (u,))
            yield Request(u, callback=self.parse_doc)

    def parse_doc(self, response):
        hxs = HtmlXPathSelector(response)

        item = RedBlueItem()
        item['url'] = response.url
        title = hxs.select("//h3[contains(@class, 'entry-title')]/text()").extract()
        if (len(title) == 0):
            log.msg("Ignored without title %s" % (response.url,))
            return None

        item['title'] = self.clean_html(title[0])
        paragraphs1 = hxs.select("//div[contains(@class, 'entry-content')]/text()").extract()
        paragraphs2 = hxs.select("//div[contains(@class, 'entry-content')]/p/text()").extract()
        item['clean_text'] = item['title'] + ' ' + self.clean_html(' '.join(paragraphs1 + paragraphs2))

        return item
