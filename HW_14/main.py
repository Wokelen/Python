from flask import Flask, url_for, request, redirect, jsonify
from utils import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/')
def main_page():
    form = """<h1 ">Поищем фильмы по названию :<h1>
    <form action="/movie/<title>" method = "post">
    <input type="text" name="title">
    <input type="submit" value ="Найти фильм">
    </form>
    <h1 ">Поищем фильмы по годам : <h1>
     <form action="/movie/year/to/year" method = "post">
     <label> введите год с </label>
    <input type="text" name="year_1">
    <label> введите год по </label>
    <input type="text" name="year_2">
    <input type="submit" value ="Найти фильм">
    </form>
    <h1 ">Поищем фильмы по аудитории :<h1>
    <form action="/rating/<audience>" method = "post"> 
    <label> введите рейтинг фильма </label>
    <input type="text" name="rating">
    <input type="submit" value ="Найти фильм">
    </form>
    <h1 ">Поищем фильмы по жанру :<h1>
    <form action="/genre/<genre>" method = "post"> 
    <label> введите жанр фильма </label>
    <input type="text" name="genre">
    <input type="submit" value ="Найти фильм">
    </form>
    
    """
    return form

@app.route('/movie/<title>', methods=["POST"])
def movie_page(title):
    recieved_data = request.form["title"]
    data = choose_title(recieved_data)
    return data

@app.route('/movie/year/to/year', methods=["POST"])
def search_page():
    recieved_data_1 = request.form['year_1']
    recieved_data_2 = request.form['year_2']
    data = find_movies(int(recieved_data_1), int(recieved_data_2))
    return data

@app.route('/rating/<audience>', methods=["POST"])
def audience_page(audience):
    recieved_data= request.form["rating"]
    if recieved_data == "G":
      return redirect(url_for("audience_page", audience = "children"))
    elif recieved_data =="G" or recieved_data== "PG" or recieved_data=="PG-13":
        return redirect(url_for("audience_page", audience= "family"))
    elif recieved_data == "R" or recieved_data == "NC-17":
        return redirect(url_for("audience_page", audience="adult"))
@app.route('/rating/children/')
def children_page():
    data = conv_for_child()
    return data

@app.route('/rating/family/')
def family_page():
    data = conv_for_family()
    return data

@app.route('/rating/adult/')
def adult_page():
    data = conv_for_adult()
    return data

@app.route('/genre/<genre>', methods=["POST"])
def genre_page(genre):
    recieved_data= request.form['genre']
    data = choose_genre(recieved_data)
    return data

if __name__ == "__main__":
    app.run(debug = True)