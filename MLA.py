# VERSION 0.1.2 ALPHA
''' https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas '''


# requests y json son obligatorios para trabajar con endpoints de ws
import requests
import json
from pprint import pprint as visualizar

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
    print(pedidoJson['id'])

def Exportar():
    with open("dump.json", "wb") as f:
        f.write(pedido.content)
    

RecorrerItems(seller_id, site_id)

#Filtrar()

Exportar()





