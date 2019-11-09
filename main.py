#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from scrapper import scrapper as Scr
import sys

def read_json(sitio):
    with open('sitios.json') as f:
        data = json.load(f)
        return data[sitio]

if __name__ == "__main__":
    sitio = sys.argv[1]
    print(sitio)
    if(sitio != ''):
        metadata_sitio = read_json(sitio)
        if(metadata_sitio):
            scrap = Scr()
            scrap.realizar_scrap(metadata_sitio)
    else:
        print('No ha seleccionado opcion')