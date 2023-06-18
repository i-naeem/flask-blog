from flask import Flask

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alex Hales"},
    {"id": 2, "name": "Ben Cutting"},
    {"id": 3, "name": "Steve Smith"},
]


@app.route('/')
def index():
    return "<h1> Hello World </h1>"


@app.route('/users/<int:user_id>')
def user(user_id):
    user = [u for u in users if u.get('id') == user_id]
    try:
        name = user[0].get("name")
        return f"<h1>{name}</h1>"
    except:
        return f"<h1>User Not Found</h1>"
