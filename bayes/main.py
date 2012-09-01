#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import csv
import clasification
import pickle
import json
from numpy import array

teee = '''
modificacion ley electoral hoy despertado literal llamado euskadi irratia noticia pp quiere modificar ley electoral euskadi pasar minimo exigido poder tener representacion parlamento vasco primero peque\u00f1a aclaracion reforma idea aquella formacion politica obtenga menos votos validos emitidos cuenta hora reparto esca\u00f1os decir partido saca votos bizkaia ejemplo simplemente ignore repartan esca\u00f1os resto objetivo hacer desaparecer partidos peque\u00f1os parlamento vasco adios pluralidad alguien podra pensar escribo post teoria primer afectado eb respecto aclaraciones modificacion podria aplicar caracter retroactivo asi siguientes elecciones ningun afectado eb superado barrera salvo ultimas elecciones razones pensar volvera hacer siguientes lado aunque beneficiara medida contrarios cosa triste democracia parlamento minorias pluralidad tema sigue adelante podremos hacer pararlo menos quede patente queja p d rectifico pnv posicionado asi retiro parte hablaba pnv sirva leccion hacer caso informaciones periodisticas oir protagonistas posicionarse
'''

def store_probability(p0V, p1V, pClass1, vocabList, path = 'probability.dat'):
    f = open(path, 'wb')
    data = {}
    data['p0V'] = p0V
    data['p1V'] = p1V
    data['pClass1'] = pClass1
    data['vocabList'] = vocabList
    dat = pickle.dumps(data) 
    f.write(dat)

def get_probability(path = 'probability.dat'):
    f = open(path, 'rb')
    dat = pickle.loads(f.read())
    return dat['p0V'], dat['p1V'], dat['pClass1'], dat['vocabList']

def load_data(prefex):
    posts = []
    for i in range(2):
        name = '%s_%d.json' %(prefex, i)
        left_f = open(name, 'rt')
        posts.extend(json.loads(left_f.read().decode('utf-8')))
    return posts

if __name__ == '__main__':
    left_posts = load_data('izquierda')
    right_posts = load_data('derecha')
    p0V, p1V, pClass1, vocabList = clasification.prepare_training(left_posts, right_posts)
    store_probability(p0V,p1V,pClass1,vocabList)

    import pdb;pdb.set_trace()
    p0V, p1V, pClass1, vocabList = get_probability()
    wordVector = clasification.bagOfWords2VecMN(vocabList, teee)
    print clasification.classifyNB(array(wordVector), p0V, p1V, pClass1)

