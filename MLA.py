# VERSION 0.1.3.6 ALPHA
''' https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas '''

import requests
import json
import pandas as pd
from glom import glom
from pprint import pprint as visualizar
from collections import defaultdict as dic



# estructura esperada:
# api_rest + site id + endpoint + seller_id

api_rest = "https://api.mercadolibre.com/sites/"
endpoint = "/search?seller_id="
seller_id = int(179571326)
site_id = "MLA"
filtros = ['id', 'title', 'category_id', 'name']

categorias = {}

pedido = requests.get(api_rest + site_id + endpoint + str(seller_id))
pedidoJson = pedido.json()
dataAUsar = json.loads(pedido.text)

# MELI ARG

def RecorrerItems(seller_id, site_id):
    global pedido
    global pedidoJson
    if site_id == "" and seller_id == "":
        seller_id = int(179571326)
        site_id = "MLA"
    else:
        pass
    #print("acá iria la funcion para:", seller_id, "\nen: ", site_id, "\nFormando: ")
    #print(api_rest + site_id + endpoint + str(seller_id))
    pedido = requests.get(api_rest + site_id + endpoint + str(seller_id))
    #visualizar(pedido.json()
    #visualizar(pedidoJson)

def Filtrar():
    print(pedidoJson['seller'])

def Exportar():
    with open("dump.json", "wb") as f:
        f.write(pedido.content)

def FiltrarAlpha(): #NO SIRVIO :(
    with open("dump.json") as input_file:
        origen = json.load(input_file)
    d = dic(dict)
    for item in origen:
        d[item["category_id"]].update(item)
    with open("output.json", "w") as output_file:
        json.dump(list(d.values()), output_file, indent=4)

def PandasDf():
    global pedidoJson
    print(' encontrar alguna otra forma de procesar los subindices del json en categorias')

    
    for n in range (0, 50):
        print("id: ", n)
        print (pedidoJson['results'][n]['id'])
        print("titulo: ", n)
        print (pedidoJson['results'][n]['title'])
        print("id categoria: ", n)
        print (pedidoJson['results'][n]['category_id'])
        print("---------------------------")
        n = n + 1
        #nombre en available_filters / i / values / j / name
        #segun valor id

        #por ejemplo:
        #si category_id = x entonces name = y

def categorias():
    for n in range (0, 10):
        print("categorias: ", n)
        print(pedidoJson['available_filters']['0']['values'][n]['name'])
        print("nombre: ", n)
        print("---------------------------")
        #print(pedidoJson['results'][n]['category_id'])
        n = n + 1
        
def EjecutarRecorrer():
    global seller_id
    global site_id
    print("Ignore las instrucciones para usar valores por default")
    site_id = input("Ingrese ID de site: ")
    seller_id = input("Ingrese ID de seller: ")


        
EjecutarRecorrer()
RecorrerItems(seller_id, site_id)

print(dataAUsar)

PandasDf()
# al final pandas termino siendo una extracción por terminal

# la solucion final deberia ser un export usando un diccionario por categorias

categorias()

'''

Generar un archivo de LOG que contenga los siguientes datos de
cada ítem:
a. "id" del ítem, "title" del item, "category_id" donde está
publicado, "name" de la categoría.

'''






