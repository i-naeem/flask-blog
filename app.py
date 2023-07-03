from services.PasswordGenerator import PasswordGenerator
from flask import render_template
from flask import request
from flask import Flask

app = Flask(__name__)


@app.get('/')
def app_get():
    return render_template('index.jinja', title="")


@app.post('/')
def app_post():
    length = 6
    try:
        length = int(request.form.get('password-length'))
    except Exception as e:
        print(e)

    generator = PasswordGenerator(password_length=length)
    password = generator.generate()

    return render_template('index.jinja', title="", password=password)


# About
@app.route('/about')
def about():
    return render_template('about.jinja', title="About")


# Contact
@app.route('/contact')
def contact():
    return render_template('contact.jinja', title="Contact")


if __name__ == '__main__':
    app.run(debug=True)
