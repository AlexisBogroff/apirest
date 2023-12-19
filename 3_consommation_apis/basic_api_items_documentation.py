from flask import Flask, jsonify, request
from flask_restx import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app, version='1.0', title='Ma super API', description="C'est une super API !")

# Simuler une base de données avec un dictionnaire
items = {'banana': {'price': 0.5, 'name': 'banana'},
         'apple': {'price': 1.0, 'name': 'apple'},
         'pear': {'price': 1.5, 'name': 'pear'}}


users = {}

# Ajout des paramètres qui seront attendus dans le body de la requête post de GetItem
parser_item_post = reqparse.RequestParser()
parser_item_post.add_argument('name', type=str, required=True, help='Name of the item')
parser_item_post.add_argument('price', type=int, required=True, help='Price of the item')

# Ajout des paramètres qui seront attendus dans le body de la requête post de PersoInfo pour la méthode Post
parser_perso_info_create = reqparse.RequestParser()
parser_perso_info_create.add_argument('user', type=str, required=True, help='Name of the user')
parser_perso_info_create.add_argument('pssd', type=str, required=True, help='Password of the user')

# Ajout des paramètres qui seront attendus dans le body de la requête post de PersoInfo pour la méthode Get
parser_perso_info_get = reqparse.RequestParser()
parser_perso_info_get.add_argument('user', type=str, required=True, help='Name of the user')



# GET - Récupérer tous les items
@api.route('/get_items')
class GetItems(Resource):
    @api.doc(description="Récupérer tous les items")
    def get(self):
        return items, 200


# GET - Récupérer un item
@api.route('/get_item/<string:name>', methods=['GET'])
class GetItem(Resource):
    @api.doc(description="Récupérer un item")
    def get(self, name):
        try:
            item = items[name]
            return item, 200
        except KeyError:
            return {'message': 'Item not found'}, 404

# POST - Créer un item
@api.route('/create_item/', methods=['POST'])
class CreateItem(Resource):
    @api.doc(description="Créer un item", parser = parser_item_post)
    def post(self):
        args = parser_item_post.parse_args()
        name, price = args['name'], args['price']
        if name in items:
            return {'message': 'Item already exists'}, 400
        item = {'price': price, 'name': name}
        items[name] = item
        return item, 201

# PUT - Mettre à jour un item existant, en réutilisant les paramètres
# de la requête post (mais URI différente)
@api.route('/put_item', methods=['PUT'])
class PutItem(Resource):
    @api.doc(description="Mettre à jour un item", parser = parser_item_post)
    def put(self):
        args = parser_item_post.parse_args()
        name, price = args['name'], args['price']
        if name not in items:
            return {'message': 'Item not found'}, 404

        items[name]['price'] = price
        return items[name], 200

# DELETE - Supprimer un item
@api.route('/delete_item/<string:name>', methods=['DELETE'])
class DeleteItem(Resource):
    @api.doc(description="Supprimer un item")
    def delete(self, name):
        if name not in items:
            return {'message': 'Item not found'}, 404

        del items[name]
        return {'message': 'Item deleted'}, 200
    
# DELETE - Supprimer tous les items
@api.route('/delete_items/', methods=['DELETE'])
class DeleteItems(Resource):
    @api.doc(description="Supprimer tous les items")
    def delete(self):
        global items
        items = {}
        return {'message': 'All items deleted'}, 200



# Utilisateur : get et post dans la même classe avec des parseurs différents
@api.route('/perso_info', methods=['GET', 'POST'])
class PersoInfo(Resource):
    @api.doc(description="Création utilisateur", parser = parser_perso_info_create)
    def post(self):
        args = parser_perso_info_create.parse_args()
        user, pssd = args['user'], args['pssd']

        if user in users:
            return {'message': 'User already exists'}, 400
        else:
            users[user] = pssd
            return {'user': user, 'pssd': pssd}, 201

    @api.doc(description="Récupération des infos utilisateur", parser = parser_perso_info_get)
    def get(self):
        args = parser_perso_info_get.parse_args()
        user = args['user']

        # Check if exists
        if user not in users:
            return {'message': 'User not found'}, 404
        else:
            return {'user': user, 'pssd': users[user]}, 200


if __name__ == '__main__':
    app.run(debug=True)
