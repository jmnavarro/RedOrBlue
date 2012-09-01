# coding: utf-8
from scrapy import log
from redorblue.redblue_spider import RedBlueSpider
from redorblue.redblue_items import RedBlueItem
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector


class NoticiasPPSpider(RedBlueSpider):
    name = "noticiaspp"
    allowed_domains = ["www.pp.es"]
    start_urls = [
        "http://www.pp.es/actualidad"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow='www.pp.es/actualidad-noticia/[a-z_0-9-]+..html'), callback='parse_doc', follow=True),
    )

    def parse_doc(self, response):
        hxs = HtmlXPathSelector(response)

        item = RedBlueItem()
        item['url'] = response.url
        t1 = hxs.select("//span[@class='texto_entradilla2']/text()").extract()
        if (len(t1) == 0):
            log.msg("Ignored without title %s" % (response.url,))
            return None

        item['title'] = self.clean_html(t1[0])
        paragraphs = hxs.select("//div[@id='columna_izquierda']/div[@class='texto_15_gris']").extract()
        item['clean_text'] = self.clean_html(' '.join(paragraphs))

        return item
