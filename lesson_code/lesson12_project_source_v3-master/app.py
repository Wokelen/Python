from flask import Flask, request, render_template, send_from_directory


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

from main import main_blueprint
from loader import loader_blueprint
app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)





@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

