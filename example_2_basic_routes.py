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
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


if __name__ == "__main__":
    app.run()