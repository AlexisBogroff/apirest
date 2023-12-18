from flask import Flask, jsonify, request

app = Flask(__name__)

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

# PUT - Mettre à jour un item existant
@app.route('/item/<string:name>', methods=['PUT'])
def update_item(name):
    if name not in items:
        return jsonify({'message': 'Item not found'}), 404

    items[name]['data'] = request.json
    return jsonify(items[name])

# DELETE - Supprimer un item
@app.route('/item/<string:name>', methods=['DELETE'])
def delete_item(name):
    if name not in items:
        return jsonify({'message': 'Item not found'}), 404

    del items[name]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
