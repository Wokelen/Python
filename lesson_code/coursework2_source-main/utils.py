import json
"""def get_posts():
	with open("data/posts.json", "r", encoding="utf-8") as file:
	  posts = json.load(file)
	return posts

def get_comments():
	with open("data/comments.json", "r", encoding="utf-8") as file:
	  comments = json.load(file)
	return comments

def get_posts_all():
	return get_posts()

def get_post_by_pk(uid):
	posts = get_posts()
	for post in posts:
		if post["pk"] == uid:
			return post

def get_posts_by_user(user_name):
	user_posts = []
	posts = get_posts()
	for post in posts:
		if post["poster_name"] == user_name:
			user_posts.append(post["content"])


	return user_posts

def get_comments_by_post_id(post_id):
	user_comments = []
	comments = get_comments()
	for comment in comments:
		if comment["post_id"] == post_id:
			user_comments.append(comment["comment"])
	return user_comments

def search_for_posts(query):
	posts_found = []
	posts = get_posts()
	for post in posts:
		if query in post["content"]:
			posts_found.append(post)
	return posts_found """

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








