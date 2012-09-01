# coding: utf-8
from scrapy import log
from redorblue.redblue_spider import RedBlueSpider
from redorblue.redblue_items import RedBlueItem
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.utils.url import urljoin_rfc
from scrapy.utils.response import get_base_url


class DocumentosIUSpider(RedBlueSpider):
    name = "documentosiu"
    allowed_domains = ["www.izquierda-unida.es", "izquierda-unida.es"]
    start_urls = [
        "http://www.izquierda-unida.es/documentos"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow='/documentos\?page=\d+', restrict_xpaths=("//ul[@class='pager']/li[@class='pager-item']", )), callback='parse_index', follow=True),
        Rule(SgmlLinkExtractor(allow='/node/\d+$', restrict_xpaths=("//div[@id='articulo1']/h2[@class='titulo']", )), callback='parse_doc', follow=True),
    )

    def parse_index(self, response):
        hxs = HtmlXPathSelector(response)
        urls = hxs.select("//div[@id='articulo1']/h2[@class='titulo']/a/@href").extract()
        log.msg('Found %i items' % (len(urls),))
        for u in urls:
            abs_u = urljoin_rfc(get_base_url(response), u)
            log.msg('Enqueue %s (%s)' % (u, abs_u))
            yield Request(abs_u, callback=self.parse_doc)

    def parse_doc(self, response):
        hxs = HtmlXPathSelector(response)

        item = RedBlueItem()
        item['url'] = response.url
        t1 = hxs.select("//div[@class='left-corner']/h2/text()").extract()
        if (len(t1) == 0):
            log.msg("Ignored without title %s" % (response.url,))
            return None

        item['title'] = self.clean_html(t1[0])
        paragraphs = hxs.select("//div[contains(@class, 'node')]/div[contains(@class, 'content')]").extract()
        paragraphs = ' '.join(paragraphs).split('\n')
        for idx, val in enumerate(paragraphs):
            if 'Adjuntos:' in val:
                paragraphs = paragraphs[:idx]
        item['clean_text'] = self.clean_html(' '.join(paragraphs))

        if len(item['clean_text']) > 10:
            return item
        else:
            return None
