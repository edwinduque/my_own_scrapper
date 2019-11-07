import requests
import bs4
import re

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
    
    def leer_vinculos(self, configuracion):
        lista_de_noticias = self.obtener_datos_del_Home(configuracion["site"],configuracion["newshref"] )
        articulos =[]
        if(lista_de_noticias):
            if(len(lista_de_noticias)>0):
                for link_noticia in lista_de_noticias:
                    articulo = self.ObtenerArticulo(link_noticia):
                    if(articulo and articulo.body != "" and articulo.title != ""):
                        articulos.append(articulo)
        print(len(articulos))


    def ObtenerArticulo(self, link):
        pass


        

