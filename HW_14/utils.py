import sqlite3

def conv_for_title():
    with sqlite3.connect("netflix.db") as con:
        con = sqlite3.connect("netflix.db")
        cur = con.cursor()

        query = """SELECT title, country, release_year, listed_in, description
                        FROM netflix
                        ORDER BY release_year DESC"""
        cur.execute(query)
        result = cur.fetchall()
        new_list = []
        for i in result:
            film = {"title" : i[0],"country": i[1], "release_year": i[2],
                    "genre": i[3], "description": i[4]}
            new_list.append(film)
        return new_list


def choose_title(title):
      data = conv_for_title()
      for row in data:
          if row['title'] == title:
              return row

def conv_for_year():
    with sqlite3.connect("netflix.db") as con:
        con = sqlite3.connect("netflix.db")
        cur = con.cursor()

        query = """SELECT title, release_year
                   FROM netflix 
                   ORDER BY release_year DESC
                   LIMIT 100 OFFSET 100
                    
                       """
        cur.execute(query)
        result = cur.fetchall()
        new_list = []
        for i in result:
            film = {"title": i[0],  "release_year": i[1]}
            new_list.append(film)
        return new_list

def find_movies(year_1, year_2):
    data = conv_for_year()
    data_list = []
    for row in data:
        if int(row["release_year"]) in range(year_1, year_2 +1):
            data_list.append(row)
    return data_list


def conv_for_child():
    with sqlite3.connect("netflix.db") as con:
        con = sqlite3.connect("netflix.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        query = """SELECT title, rating, description
                   FROM netflix
                   WHERE rating == "G"
                   """
        cur.execute(query)
        result = cur.fetchall()
        count = 0
        new_list = []
        for row in result:
            item = result[count]
            new_dict = {}
            for key in item.keys():
                count += 1
                new_dict[key] = item[key]
            if count >= len(result):
                break
            new_list.append(new_dict)
        return new_list


def conv_for_family():
    with sqlite3.connect("netflix.db") as con:
        con = sqlite3.connect("netflix.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        query = """SELECT title, rating, description
                   FROM netflix
                   WHERE rating = "G" OR rating = "PG" OR rating = "PG-13"
                   """
        cur.execute(query)
        result = cur.fetchall()
        count = 0
        new_list = []
        for row in result:
            item = result[count]
            new_dict = {}
            for key in item.keys():
                count += 1
                new_dict[key] = item[key]
            if count >= len(result):
                break
            new_list.append(new_dict)
        return new_list

def conv_for_adult():
    with sqlite3.connect("netflix.db") as con:
        con = sqlite3.connect("netflix.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        query = """SELECT title, rating, description
                   FROM netflix
                   WHERE rating = "R" OR rating = "NC-17" 
                   """
        cur.execute(query)
        result = cur.fetchall()
        count = 0
        new_list = []
        for row in result:
            item = result[count]
            new_dict = {}
            for key in item.keys():
                count += 1
                new_dict[key] = item[key]
            if count >= len(result):
                break
            new_list.append(new_dict)
        return new_list

def conv_for_genre():
    with sqlite3.connect("netflix.db") as con:
        con = sqlite3.connect("netflix.db")
        cur = con.cursor()

        query = """SELECT title, listed_in, description, release_year
                        FROM netflix  
                        ORDER by release_year DESC
                        LIMIT 10
                        """
        cur.execute(query)
        result = cur.fetchall()
        new_list = []
        for i in result:
            film = {"title" : i[0],"genre": i[1], "description": i[2]}
            new_list.append(film)
        return new_list


def choose_genre(genre):
    data = conv_for_genre()
    g_list = []
    for row in data:
        if  genre in row["genre"]:
            del row["genre"]
            g_list.append(row)
    return g_list

def choose_actors(actor_1, actor_2):
    with sqlite3.connect("netflix.db") as con:
        con = sqlite3.connect("netflix.db")
        cur = con.cursor()

        query = f"""SELECT  netflix.cast
                        FROM netflix  
                        WHERE netflix.cast LIKE "%{actor_1}%" AND netflix.cast LIKE "%{actor_2}%"
                        GROUP BY netflix.cast
                        """
        cur.execute(query)
        result = cur.fetchall()
        actor_list =[]
        new_act_list = []
        max_list = []

        for row in result:
            for name in row:
                n = name.split(",")
                actor_list.append(n)
        for row in actor_list:
            for name in row:
                new_act_list.append(name)

        for row in new_act_list:
            count = 0
            for name in new_act_list:
                if name == row :
                    count +=1
                    if count>2 and name !=actor_1 and name !=actor_2:
                      max_list.append(name)
        act_set = set(max_list)

        return list(act_set)

def choose_movie(type, release_year, genre):
    with sqlite3.connect("netflix.db") as con:
        con = sqlite3.connect("netflix.db")
        cur = con.cursor()

        query = f"""SELECT  type, title, release_year, listed_in
                        FROM netflix  
                        WHERE type = "{type}" AND release_year = "{release_year}"
                        AND listed_in LIKE "%{genre}%"
                        """
        cur.execute(query)
        result = cur.fetchall()
        return result


