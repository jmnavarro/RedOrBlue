# coding: utf-8
from scrapy import log
from redorblue.redblue_spider import RedBlueSpider
from redorblue.redblue_items import RedBlueItem
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request


class BoletinUISpider(RedBlueSpider):
    name = "boletin_iu"
    allowed_domains = ["www.izquierda-unida.es", "izquierda-unida.es"]
    start_urls = [
        "http://www.izquierda-unida.es/boletin"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow='www.izquierda-unida.es/ftp/boletin_[0-9]+.htm$'), callback='parse_boletin', follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths=("//div[@id='titular']/a/@href",)), callback='parse_doc', follow=True)
    )

    def parse_boletin(self, response):
        hxs = HtmlXPathSelector(response)
        urls = hxs.select("//div[@id='titular']/a/@href").extract()
        log.msg('Found %i items' % (len(urls),))
        for u in urls:
            log.msg('Enqueue %s' % (u,))
            yield Request(u, callback=self.parse_doc)

    def parse_doc(self, response):
        if not 'izquierda-unida.es/node/' in response.url:
            log.msg("Ignored %s" % (response.url,))
            return None

        hxs = HtmlXPathSelector(response)

        item = RedBlueItem()
        item['url'] = response.url
        title = hxs.select("//div[@id='articulo_pagina']/div[@class='node']/div[@class='node-left']/h2/text()").extract()
        if (len(title) == 0):
            log.msg("Ignored without title %s" % (response.url,))
            return None

        item['title'] = self.clean_html(title[0])
        paragraphs = hxs.select("//div[@id='articulo_pagina']/div[@class='node']/div[@class='node-left']/div[contains(@class, 'content')]/p").extract()
        item['clean_text'] = self.clean_html(' '.join(paragraphs))

        return item
