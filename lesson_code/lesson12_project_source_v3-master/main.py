from flask import render_template, Blueprint, request
from functions import *

main_blueprint = Blueprint('main_blueprint',__name__,template_folder='templates', url_prefix = "/")

# Добавим render_template
@main_blueprint.route('/')
def main_page():
    return render_template("index.html")

@main_blueprint.route('/search')
def search_page():
    substr = request.args.get("s")
    posts = search_post(substr)
    return render_template("post_list.html", posts = posts, substr = substr)