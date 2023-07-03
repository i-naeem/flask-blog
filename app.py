from flask import Flask
from flask import render_template

app = Flask(__name__)


# Home Route
@app.route('/')
def home():
    return render_template('index.jinja')


if __name__ == '__main__':
    app.run(debug=True)
