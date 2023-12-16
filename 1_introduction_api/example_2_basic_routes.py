from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Route basique
@app.route('/login')
def login():
    return 'login'

# Route avec paramètre (variable)
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# Route avec paramètre converti (en int)
@app.route('/ht_to_ttc/<int:prix_ht>')
def ht_to_ttc(prix_ht):
    print(type(prix_ht))
    return f"Prix TTC: {prix_ht * 1.2}€"


# Passage de plusieurs paramètres
@app.route('/user/<username>/<int:age>')
def user(username, age):
    return f'{username} is {age} years old'


# Passage de paramètres optionnels
# Inscrite dans la fonction et non dans la route
@app.route('/user/optn/<username>/<int:size>/<int:weight>')
@app.route('/user/optn/<username>/<int:size>')
def user_properties(username, size, weight=None):
    if weight:
        return f'{username} is {size} tall and weighs {weight}'
    else:
        return f'{username} is {size} tall'


# Passage de paramètres optionnels avec valeur par défaut
# Inscrite dans la route et non dans la fonction
@app.route('/blog/page/', defaults={'page': 1})
@app.route('/blog/page/<int:page>')
def blog(page):
    return f'Page du blog {page}'



if __name__ == "__main__":
    app.run()