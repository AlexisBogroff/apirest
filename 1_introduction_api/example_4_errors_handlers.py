from flask import Flask, jsonify, request
import time
import logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)


app = Flask(__name__)

# Simuler une base de données avec un dictionnaire
items = {}

# ROUTES
# ------

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


# GENERATION D'ERREURS
# --------------------

# Fonction très lente
@app.route('/timeout3s')
def timeout3s():
    time.sleep(4)
    return {'|message|': '|| 4s ||'}, 200


@app.route('/exception')
def exception():
    raise Exception('|| Exception ||')


@app.route('/type_error/<val>')
def value_error(val):
    # Cette fonction va casser dès lors qu'on lui passe une
    # val qui n'est pas une liste. Cela va donc générer 
    # un TypeError lors de l'addition (qu'on gère plus bas avec le handler)
    val + [2]
    return jsonify({'|message|': '|| Tout ne fonctionne pas si bien ||'}), 200


from flask import abort
@app.route('/401')
def error_401():
    abort(401, description='|| 401  recup||')


# @app.route('/401')
# def error_401():
#     return jsonify({'|message|': '|| 401 ||'}), 401


@app.route('/403')
def error_403():
    # Nous utilisons abort pour générer une erreur
    # qui sera gérée par le handler et, étant considérée
    # par Flask comme une erreur, elle sera loguée
    abort(403, description='|| 403 ||')


@app.route('/405')
def error_405():
    # Nous utilisons encore abort pour générer une erreur
    # qui sera gérée par son handler respectif
    abort(405, description='|| 405 ||')

from flask import Response
from flask import stream_with_context
@app.route('/stream')
def stream_example():
    def generate():
        yield 'Hello '
        yield 'World!'
    return Response(stream_with_context(generate()))




# Gestion des erreurs courantes
# Et des erreurs qui peuvent survenir de manière inattendue
# ex: erreur de syntaxe dans le code ou une ValueError
# (la fonction avec l'erreur n'aura pas forcément prévu de gérer l'erreur)
# -----------------------------
# (ne pas faire attention aux codes
# erreurs dans ces exemples)
# -----------------------------

# Toutes les erreurs seront loggées grâce à logging


# Message qui sera loggé, non personalisé, et renvoyé au client tel quel
@app.errorhandler(401)
def handle_exception_401(error):
    return f"Pas de chance vous tombez sur une erreur : {error}", 401


# Message qui sera loggé, non personalisé, et renvoyé au client tel quel
@app.errorhandler(403)
def handle_exception_403(error):
    return error, 403


# En production, un bon gestionnaire d'exceptions
# enregistre des informations sur l'erreur tout en renvoyant
# une réponse générique au client pour ne pas donner de
# détails sur la structure interne de l'application
@app.errorhandler(405)
def handle_exception_405(error):
    # Log dans un fichier
    print(error)
    # Inscription du message d'erreur personalisé dans le fichier error.log
    logging.error('|| PARIS BRUUUUULE || %s', (error))
    return "|| Tout va bien, nous gérons le problème :) ||", 405


# Flask considère toute exception non capturée et non gérée
# comme une erreur interne du serveur (donc 500, ce qui est logique).
# Nous pouvons cependant gérer ces erreurs avec un handler pour
# les créer un message spécifique
@app.errorhandler(TypeError)
def handle_type_error(e):
    return "|| Type Error ||", 500



if __name__ == '__main__':
    app.run(debug=True)
