from flask import Flask, jsonify
import example_5_fonctions as fcts

app = Flask(__name__)

# GET - Créer des items aléatoires
@app.route('/generate_data')
def generate_data():
    random_items = fcts.random_fill()
    fcts.save_items(random_items)
    return jsonify(random_items)


# GET - Calculer le prix total de tous les items
@app.route('/total_price')
def get_total_price():
    items = fcts.get_items()
    total_cost = fcts.calcul_prix_total(items)
    return jsonify(total_cost)
