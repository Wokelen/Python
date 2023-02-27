import json


def load_data(file_name):
	with open(file_name, encoding="utf-8") as file:
		data = json.load(file)
	return data

def load_posts(search_word = None, user_name = None):
	posts = load_data("data/posts.json")
	if search_word:
		posts = filter(lambda x : search_word in x["content"].lower(),posts)
	if user_name:
		posts = filter(lambda x : user_name == x["poster_name"].lower(),posts)
	return posts

def load_post(pk):
	posts = load_posts()
	for post in posts:
		if post["pk"] == pk:
			return post

def load_comments(post_pk):
	all_comments = load_data("data/comments.json")
	comments = []
	for comm in all_comments:
		if comm["post_id"] == post_pk:
			comments.append(comm)
	return comments








