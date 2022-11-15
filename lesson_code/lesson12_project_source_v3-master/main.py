from flask import render_template, Blueprint, request
from functions import *

main_blueprint = Blueprint('main_blueprint',__name__,template_folder='templates', url_prefix = "/")

# Добавим render_template
@main_blueprint.route('/')
def view_posts():
    return render_template("index.html")

@main_blueprint.route('/<int:pk>')
def view_posts(pk):

    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug = True)