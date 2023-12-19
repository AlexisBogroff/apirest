from flask import Flask, jsonify, request
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app, version='1.0', title='Ma super API', description="C'est une super API !")


# Simuler une base de données avec un dictionnaire
items = {'banana': {'price': 0.5, 'name': 'banana'},
         'apple': {'price': 1.0, 'name': 'apple'},
         'pear': {'price': 1.5, 'name': 'pear'}}


# Reqparse pour post
parser_item_post = reqparse.RequestParser()
parser_item_post.add_argument('name', type=str, required=True, help='Name of the item')
parser_item_post.add_argument('price', type=int, required=True, help='Price of the item')

# Reqparse pour get
parser_item_get = reqparse.RequestParser()
parser_item_get.add_argument('name', type=str, required=True, help='Name of the item')


# GET - Récupérer tous les items
@api.route('/items', methods=['GET'])
class GetItem(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.status_code = 200
    
    @api.doc(description="Hello, ceci est une nouvelle description pour notre méthode Get")
    def get(self):
        return items, self.status_code


# GET - Récupérer un item
@api.route('/item/<string:name>', methods=['GET'])
class GetItem(Resource):
    
    @staticmethod
    def get(name):
        if name in items:
            item = items[name]
            return item
        return {'message': 'Item not found'}, 404

# POST - Créer un nouvel item
@api.route('/item/<string:name>/<int:price>', methods=['PUT'])
class PutItem(Resource):
    
    @staticmethod
    def put(name, price):
        if name not in items:
            return {'message': 'Item not found'}, 404

        items[name]['data'] = price
        return items[name]



@api.route('/item', methods=['POST'])
class CreateItem(Resource):
    
    @staticmethod
    @api.expect(parser_item_post)
    def post():
        args = parser_item_post.parse_args()
        name = args['name']
        price = args['price']

        if name in items:
            return {'message': 'Item already exists'}, 400

        item = {'name': name, 'data': price}
        items[name] = item
        return item, 201


# DELETE - Supprimer un item
@api.route('/item', methods=['DELETE'])
class DeleteItem(Resource):

    @staticmethod
    def return_message(status_code, message_del='Item deleted', message_not_found='Item not found'):
        if status_code == 200:
            return {'message': message_del}, 200
        else:
            return {'message': message_not_found}, 404
    
    @api.expect(parser_item_get)
    def delete(self):
        name = request.args.get('name')

        if name not in items:
            return self.return_message(404, message_not_found='SPECIFIC MESSAGE')

        del items[name]
        return self.return_message(200)
    


if __name__ == '__main__':
    app.run(debug=True)
