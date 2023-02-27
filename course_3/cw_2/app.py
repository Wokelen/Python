from flask import Flask, render_template, jsonify, request
from utils import *
import logger
app = Flask(__name__)

log = logger.get_logger("api")


@app.route('/')
def view_posts():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:pk>')
def view_post(pk):
    post = load_post(pk)
    comments = load_comments(pk)
    return render_template("post.html", post=post, comments=comments)


@app.route('/search/')
def search_post():
    word = request.args.get("s", " ").lower()
    posts = load_posts(search_word=word)
    return render_template("index.html", posts=posts)


@app.route('/user/<user_name>')
def user_post(user_name):

    posts = load_posts(user_name=user_name)
    return render_template("user-feed.html", posts=posts)


@app.route('/api/')
def api_posts():
    posts = load_posts()
    log.info(f"api_posts = > {len(posts)}")
    return jsonify(posts)


@app.route('/api/post/<int:pk>')
def api_post(pk):
    post = load_post(pk)
    log.info(f"api_post = > {pk}")
    return jsonify(post)


@app.errorhandler(500)
def server_error(e):
    return "Программа не смогла выполнить ваш запрос, обратитесь к администратору"


@app.errorhandler(404)
def server_error(e):
    return "Вы ввели неправильные данные (ошибка 404)"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=25000)


