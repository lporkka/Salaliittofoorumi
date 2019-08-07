from flask import render_template, request, url_for, redirect

from application import app, db
from application.posts.models import Post
from application.posts.forms import PostForm


@app.route("/posts", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts=Post.query.all())


@app.route("/posts/new/")
def posts_form():
    return render_template("posts/new.html", form=PostForm())


@app.route("/posts/", methods=["POST"])
def posts_create():
    form = PostForm(request.form)

    p = Post(form.content.data)

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("posts_index"))
