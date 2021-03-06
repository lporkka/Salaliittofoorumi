from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.posts.models import Post
from application.posts.forms import PostForm


@app.route("/posts", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts=Post.query.all())


@app.route("/posts/new/")
@login_required
def posts_form():
    return render_template("posts/new.html", form=PostForm())


@app.route("/posts/", methods=["POST"])
@login_required
def posts_create():
    form = PostForm(request.form)
    thread_id = int(request.args.get('thread_id'))
    p = Post(form.content.data,
             account_id=current_user.id,
             thread_id=thread_id)

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("get_thread", thread_id=thread_id))
