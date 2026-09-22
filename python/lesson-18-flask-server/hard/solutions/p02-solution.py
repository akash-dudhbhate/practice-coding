"""SOLUTION: Flask with Jinja2 templates (Hard)"""
from flask import Flask, render_template_string, request, redirect
from jinja2 import DictLoader

app = Flask(__name__)

BASE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>{% block title %}My Blog{% endblock %}</title></head>
<body>
  <nav><a href="/">Home</a> | <a href="/new">New Post</a></nav>
  {% block content %}{% endblock %}
</body>
</html>
"""

INDEX_TEMPLATE = "{% extends 'base.html' %}{% block content %}<h1>Posts</h1>{% for p in posts %}<p><a href='/post/{{p.id}}'>{{p.title}}</a></p>{% endfor %}{% endblock %}"

POST_TEMPLATE = "{% extends 'base.html' %}{% block content %}<h1>{{post.title}}</h1><p>{{post.content}}</p>{% endblock %}"

NEW_POST_TEMPLATE = """{% extends 'base.html' %}{% block content %}
<h1>New Post</h1>
<form method="POST"><input name="title" placeholder="Title"><br>
<textarea name="content" placeholder="Content"></textarea><br>
<button type="submit">Create</button></form>{% endblock %}"""

# Provide 'base.html' to the Jinja loader so {% extends %} works
# even though the template lives in a Python string, not a file.
app.jinja_loader = DictLoader({"base.html": BASE_TEMPLATE})

posts = []
next_id = 1

@app.route("/")
def index():
    return render_template_string(INDEX_TEMPLATE, posts=posts, base=BASE_TEMPLATE)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "Not found", 404
    return render_template_string(POST_TEMPLATE, post=post, base=BASE_TEMPLATE)

@app.route("/new", methods=["GET", "POST"])
def new_post():
    global next_id
    if request.method == "POST":
        posts.append({"id": next_id, "title": request.form["title"], "content": request.form["content"]})
        next_id += 1
        return redirect("/")
    return render_template_string(NEW_POST_TEMPLATE, base=BASE_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)
