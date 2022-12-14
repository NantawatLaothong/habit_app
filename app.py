from flask import Flask, render_template

from model import db

# __name__ = module_name
app = Flask(__name__);

# decorator to the get_index function and is a method of the class FLASK
@app.route("/")
def get_index():
    return render_template(
        'index.html',
    message="Hello World!",
    number=34)

@app.route("/anime")
def show_title():
    return render_template(
        'anime.html',
        anime=db[0]
    )

