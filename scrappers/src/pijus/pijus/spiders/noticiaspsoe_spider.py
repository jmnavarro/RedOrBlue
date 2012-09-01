# coding: utf-8
from scrapy import log
from redorblue.redblue_spider import RedBlueSpider
from redorblue.redblue_items import RedBlueItem
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

# todas las urls extraidas acaban en %0a ¿¿??

class NoticiasPSOESpider(RedBlueSpider):
    name = "noticiaspsoe"
    allowed_domains = ["www.psoe.es"]
    start_urls = [
        "http://www.psoe.es/saladeprensa/docs/apt/4184/page/articulos-intervenciones.html"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow='/saladeprensa/docs/\d+/page/', restrict_xpaths=("//div[@class='cajita']/div[@class='promo']", )), callback='parse_doc', follow=True),
    )

    def parse_doc(self, response):
        hxs = HtmlXPathSelector(response)

        item = RedBlueItem()
        item['url'] = response.url
        t1 = hxs.select("//div[@id='cuerpo-nota']/h2/text()").extract()
        if (len(t1) == 0):
            log.msg("Ignored without title %s" % (response.url,))
            return None

        item['title'] = self.clean_html(t1[0])
        paragraphs = hxs.select("//div[@id='cuerpo-nota']").extract()
        item['clean_text'] = self.clean_html(' '.join(paragraphs))

        return item
