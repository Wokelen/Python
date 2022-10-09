import json
def load_candidates():
    with open("candidates.json", encoding = "utf-8") as file:
        new_file = json.load(file)
    return new_file

def get_all():
    all = []
    for line in load_candidates():
        all.append(line["name"])
    return all


def get_by_pk(pk):
    for line in load_candidates():
        if line["pk"] == pk:
            return line

def get_by_skills(skill_name):
    cand_list = []
    for line in load_candidates():
        if skill_name.lower() in line["skills"].lower().split(", "):
             cand_list.append(line)

    return cand_list



from flask import Flask
app = Flask(__name__)
@app.route("/")
def main_page():
    list = '<br>'
    for line in load_candidates():
        list += line['name'] + '<br>'
        list += line['position'] + '<br>'
        list += line['skills'] + '<br>'
        list += '<br>'

    return f"<pre>{list}</pre>"

@app.route("/candidates/<int:pk>")
def cand_page(pk):
    url = get_by_pk(pk)['picture']
    list = '<br>'
    list += f"<img src='({url})'>" + '<br>'
    list += get_by_pk(pk)['name'] + '<br>'
    list += get_by_pk(pk)['position'] + '<br>'
    list += get_by_pk(pk)['skills'] + '<br>'
    list += '<br>'
    return f"<pre>{list}</pre>"

@app.route("/skills/<skill_name>")
def skills_page(skill_name):
    list = '<br>'
    for line in get_by_skills(skill_name):
        list += line['name'] + '<br>'
        list += line['position'] + '<br>'
        list += line['skills'] + '<br>'
        list += '<br>'
    return f"<pre>{list}</pre>"

app.run()