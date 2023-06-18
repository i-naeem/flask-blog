from flask import Flask
from flask import url_for

app = Flask(__name__)


# Home Route
@app.route('/')
def home():
    return "<h1> Hello World </h1>"


@app.route('/about')
def about():
    return "<h1> About </h1>"


@app.route('/contact')
def contact():
    return "<h1> Contact </h1>"


if __name__ == '__main__':
    app.run(debug=True)
