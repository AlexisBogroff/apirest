import random
import json
from settings import PATH_DATA

# Fonctions de calcul
# -------------------
def calcul_prix_total(items):
    total_price = sum(map(lambda item: item['data']['price'], items.values()))
    return {'total_price': total_price}

def random_fill():
    items = {}
    for i in range(10):
        item = {'name': f'item{i}', 'data': {'price': random.randint(1, 10)}}
        items[item['name']] = item
    return items
# -------------------

# Fonctions de gestion des données
# --------------------------------
def get_items():
    """ Get data """
    with open(PATH_DATA, 'r') as file:
        items = json.load(file)
    return items

def save_items(items):
    """ Save data """
    with open(PATH_DATA, 'w') as file:
        json.dump(items, file, indent=4)
# --------------------------------