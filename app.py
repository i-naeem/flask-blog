from flask import Flask
from flask import render_template

app = Flask(__name__)


# Home Route
@app.route('/')
def home():
    return render_template('index.html', name="Mr. Robot")


@app.route('/user')
def about():
    return "<h1> About </h1>"


@app.route('/contact')
def contact():
    return "<h1> Contact </h1>"


if __name__ == '__main__':
    app.run(debug=True)
