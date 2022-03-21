from flask import Flask, redirect, request, render_template, session
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions
app.secret_key = "DEV"

@app.route('/')
def display_homepage():
    return render_template('bootstrap.html')

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port='5002',
        use_reloader=True,
        use_debugger=True,
    )