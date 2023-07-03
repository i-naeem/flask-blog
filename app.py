from services.PasswordGenerator import PasswordGenerator
from flask import render_template
from flask import request
from flask import Flask

app = Flask(__name__)


# Home Route
@app.route('/')
def home():
    return render_template('index.jinja', current_route="/about")


# About
@app.route('/about')
def about():
    return render_template('about.jinja')


# Contact
@app.route('/contact')
def contact():
    return render_template('contact.jinja')


@app.route('/generator', methods=["POST"])
def generator():
    length = 6
    try:
        length = int(request.form.get('password-length'))
    except Exception as e:
        print(e)

    generator = PasswordGenerator(password_length=length)
    password = generator.generate()

    return dict(password=password)


if __name__ == '__main__':
    app.run(debug=True)
