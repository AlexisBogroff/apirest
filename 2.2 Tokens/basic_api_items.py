import os
from flask import Flask, jsonify, request
import jwt
from functools import wraps


app = Flask(__name__)

# Configuration de la clé
app.config['USERNAME'] = 'alex'
app.config['SECRET_KEY'] = 'password'

# Simuler une base de données avec un dictionnaire
items = {}

# GET - Récupérer tous les items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# GET - Récupérer un item
@app.route('/item/<string:name>', methods=['GET'])
def get_item(name):
    item = items.get(name)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# POST - Créer un nouvel item
@app.route('/item/<string:name>', methods=['POST'])
def create_item(name):
    if name in items:
        return jsonify({'message': 'Item already exists'}), 400

    item = {'name': name, 'data': request.json}
    items[name] = item
    return jsonify(item), 201



# ----------------- AUTHENTIFICATION ----------------- #

def expiration_date():
    return datetime.datetime.utcnow() + datetime.timedelta(minutes=1)

import datetime
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth and auth.username == app.config['USERNAME'] and auth.password == app.config['SECRET_KEY']:
        token = jwt.encode({'user': auth.username, 'exp': expiration_date()}, app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return jsonify({'message': 'Could not verify'}), 403


def token_required(f):
    @wraps(f)  # permet d'attribuer le décorateur à plusieurs fonctions
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            print(data)
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorator

# ---------------------------------------------------- #


# Test route
@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'ACCESS GRANTED'}), 200


# PUT - Mettre à jour un item existant
@app.route('/item/<string:name>', methods=['PUT'])
@token_required
def update_item(name):
    if name not in items:
        return jsonify({'message': 'Item not found'}), 404

    items[name]['data'] = request.json
    return jsonify(items[name])


# DELETE - Supprimer un item
@token_required
@app.route('/del_item/<string:name>', methods=['DELETE'])
def delete_item(name):
    print(name)
    if name not in items:
        return jsonify({'message': 'Item not found'}), 404
    
    del items[name]
    return jsonify({'message': 'Item deleted'}), 200


# DELETE - Supprimer tous les items
@app.route('/del_items', methods=['DELETE'])
@token_required
def delete_items():
    items.clear()
    return jsonify({'message': 'All items deleted'}), 200





if __name__ == '__main__':
    app.run(debug=True)
