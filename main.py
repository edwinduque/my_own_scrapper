#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from scrapper import scrapper as Scr

def read_json():
    with open('sitios.json') as f:
        data = json.load(f)
        return data["elespectador"]

if __name__ == "__main__":
    metadata_sitio = read_json()
    scrap = Scr()
    scrap.leer_vinculos(metadata_sitio)