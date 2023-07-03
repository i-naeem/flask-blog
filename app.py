from services.PasswordGenerator import PasswordGenerator
from flask import render_template
from flask import request
from flask import Flask

app = Flask(__name__)


@app.get('/')
def app_get():
    return render_template(
        'index.jinja',
        title="",
        case=0,
    )


@app.post('/')
def app_post():
    length = 14
    character_case = 0
    try:
        length = int(request.form.get('password-length'))
        character_case = int(request.form.get('ch-case'))
    except Exception as e:
        print(e)

    generator = PasswordGenerator(
        password_length=length,
        character_case=character_case
    )

    password = generator.generate()

    return render_template(
        'index.jinja',
        title="",
        password=password,
        previous_value=length,
        case=character_case if character_case else 0,
    )


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
