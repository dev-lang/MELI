# VERSION 0.1.3.2 ALPHA
''' https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas '''


# requests y json son obligatorios para trabajar con endpoints de ws
import requests
import json
import pandas as pd
from glom import glom
from pprint import pprint as visualizar
from collections import defaultdict as dic

''' Recorrer todos los ítems publicados por el seller_id = 179571326 del
 site_id = "MLA" '''

# estructura esperada:
# api_rest + site id + endpoint + seller_id

api_rest = "https://api.mercadolibre.com/sites/"
endpoint = "/search?seller_id="
seller_id = int(179571326)
site_id = "MLA"
filtros = ['id', 'title', 'category_id', 'name']
pedido = requests.get(api_rest + site_id + endpoint + str(seller_id))
pedidoJson = pedido.json()
dataAUsar = json.loads(pedido.text)

# MELI ARG


'''

Generar un archivo de LOG que contenga los siguientes datos de
cada ítem:
a. "id" del ítem, "title" del item, "category_id" donde está
publicado, "name" de la categoría.

'''


def RecorrerItems(seller_id, site_id):
    global pedido
    global pedidoJson
    print("acá iria la funcion para:", seller_id, "\nen: ", site_id, "\nFormando: ")
    print(api_rest + site_id + endpoint + str(seller_id))
    pedido = requests.get(api_rest + site_id + endpoint + str(seller_id))
    #visualizar(pedido.json()
    #visualizar(pedidoJson)

def Filtrar():
    print(pedidoJson['seller'])

def Exportar():
    with open("dump.json", "wb") as f:
        f.write(pedido.content)

def FiltrarAlpha():
    with open("dump.json") as input_file:
        origen = json.load(input_file)
    d = dic(dict)
    for item in origen:
        d[item["category_id"]].update(item)
    with open("output.json", "w") as output_file:
        json.dump(list(d.values()), output_file, indent=4)

def PandasDf():
    global pedidoJson
    # raise ValueError("All arrays must be of the same length")
    print(' encontrar alguna otra forma de procesar los subindices del json')
    #global df
    #df = pd.read_json (r'dump.json')
    #print (df)
    #df.info()

    #df = pd.read_json('dump.json')
    #df['results'].apply(lambda row: glom(row, 'results.0.id'))
    #results.0.id / title / category_id

    
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
        
    

RecorrerItems(seller_id, site_id)

print(dataAUsar)

#Filtrar()

#Exportar()

PandasDf()
# al final pandas termino siendo una extracción por terminal




