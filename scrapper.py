import requests
import bs4
import re
from articulo import ArticlePage
import csv
import time

class scrapper():
    _is_well_formed_url= re.compile(r'^https?://.+/.+$') # i.e. https://www.somesite.com/something
    _is_root_path = re.compile(r'^/.+$') # i.e. /some-text


    def __init__(self):
        pass

    def obtener_datos_del_Home(self, url, home_filter):
        response = requests.get(url)
        response.raise_for_status()
        html = bs4.BeautifulSoup(response.text, 'html.parser')
        lista_de_anchor = html.select(home_filter)
        lista_de_titulos = []
        if(lista_de_anchor and len(lista_de_anchor) > 0):
            for anchor in lista_de_anchor:
                if anchor.has_attr('href'):
                    lista_de_titulos.append(anchor['href'])
        return lista_de_titulos
    
    def realizar_scrap(self, configuracion):
        lista_de_noticias = self.obtener_datos_del_Home(configuracion["site"],configuracion["newshref"] )
        articulos =[]
        if(lista_de_noticias):
            if(len(lista_de_noticias)>0):
                for link_noticia in lista_de_noticias:
                    link_corregido = self.corregir_url(configuracion["site"], link_noticia)
                    if(link_corregido != ''):
                        articulo = ArticlePage()
                        articulo.url = link_corregido
                        articulo = self.obtenerArticulo(articulo, configuracion["newstitle"], configuracion["newsbody"])
                        if(articulo and articulo.body != "" and articulo.title != ""):
                            articulos.append(articulo)
        if(len(articulos)>0):
            self.guardar_csv(articulos)

    def corregir_url(self, host, url):
        if(self._is_well_formed_url.match(url)):
            return url
        elif(self._is_root_path.match(url)):
            return '{host}{url}'.format(host=host, url = url)
        else:
            return ''

    def obtenerArticulo(self, articulo, filter_title, filter_body):
        response_articulo = requests.get(articulo.url)
        response_articulo.raise_for_status()
        html = bs4.BeautifulSoup(response_articulo.text, 'html.parser')
        articulo.title  = html.select(filter_title)
        articulo.body = html.select(filter_body)
        return articulo

    def guardar_csv(self, articulos):
        current_time = time.strftime(r"_%d_%m_%Y_%H_%M", time.localtime())
        with open('site_file{now}.csv'.format(now=current_time), mode='w') as articulo_file:
            articulo_writer = csv.writer(articulo_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            articulo_writer.writerow(['url', 'title', 'body'])
            for articulo in articulos:
                articulo_writer.writerow([articulo.url, articulo.title, articulo.body])

        

