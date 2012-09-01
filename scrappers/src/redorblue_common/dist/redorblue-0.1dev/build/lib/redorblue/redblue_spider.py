# coding: utf-8
#from scrapy import log
from scrapy.contrib.spiders import CrawlSpider
import re
import string


class RedBlueSpider(CrawlSpider):
    CLEAN_TAGS_RE = re.compile(r'<.*?>')
    CLEAN_SPACES_RE = re.compile(r'\s+')
    STOPWORDS_ES = ['pues', 'sino', 'si', 'solo', 'va', 'pues', 'un', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'tal', 'tanto', 'tantos', 'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'es', 'lo', 'como', 'mas', 'pero', 'sus', 'le', 'ya', 'o', 'fue', 'este', 'ha', 'si', 'porque', 'esta', 'son', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'ser', 'tiene', 'tambien', 'me', 'hasta', 'hay', 'donde', 'han', 'quien', 'estan', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'fueron', 'ese', 'eso', 'habia', 'ante', 'ellos', 'e', 'esto', 'mi', 'antes', 'algunos', 'que', 'unos', 'yo', 'otro', 'otras', 'otra', 'el', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'sea', 'poco', 'ella', 'estar', 'haber', 'estas', 'estaba', 'estamos', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tu', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os', 'mio', 'mia', 'mios', 'mias', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estas', 'esta', 'estamos', 'estais', 'estan', 'este', 'estes', 'estemos', 'esteis', 'esten', 'estare', 'estaras', 'estara', 'estaremos', 'estareis', 'estaran', 'estaria', 'estarias', 'estariamos', 'estariais', 'estarian', 'estaba', 'estabas', 'estabamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuvieramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses', 'estuviesemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habeis', 'han', 'haya', 'hayas', 'hayamos', 'hayais', 'hayan', 'habre', 'habras', 'habra', 'habremos', 'habreis', 'habran', 'habria', 'habrias', 'habriamos', 'habriais', 'habrian', 'habia', 'habias', 'habiamos', 'habiais', 'habian', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubieramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiesemos', 'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seais', 'sean', 'sere', 'seras', 'sera', 'seremos', 'sereis', 'seran', 'seria', 'serias', 'seriamos', 'seriais', 'serian', 'era', 'eras', 'eramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras', 'fueramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuesemos', 'fueseis', 'fuesen', 'siendo', 'sido', 'tengo', 'tienes', 'tiene', 'tenemos', 'teneis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengais', 'tengan', 'tendre', 'tendras', 'tendra', 'tendremos', 'tendreis', 'tendran', 'tendria', 'tendrias', 'tendriamos', 'tendriais', 'tendrian', 'tenia', 'tenias', 'teniamos', 'teniais', 'tenian', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuvieramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviesemos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened']
    PUNCTUATION_TRANS = string.maketrans(string.punctuation + '0123456789', ' ' * (len(string.punctuation) + 10))
    ACUTES = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'NTILDE'}

    def clean_html(self, str):
        ret = str.encode('utf8').lower()
        # tags
        ret = self.CLEAN_TAGS_RE.sub('', ret)
        # punctuation
        ret = ret.translate(self.PUNCTUATION_TRANS)
        # symbols
        for k in self.ACUTES:
            ret = string.replace(ret, k, self.ACUTES[k])
        # symbols
        ret = ''.join(e for e in ret if e.isalpha() or e == ' ')
        # ñ
        ret = string.replace(ret, 'NTILDE', 'ñ')
        # spaces
        ret = self.CLEAN_SPACES_RE.sub(' ', ret)
        # stopwords
        ret = ' '.join((word for word in ret.split(' ') if not word in self.STOPWORDS_ES))
        return ret.strip()

