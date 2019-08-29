import logging
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.posts.models import Post
from application.posts.forms import PostForm
from application.threads.models import Thread
from application.threads.forms import ThreadForm


@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads=Thread.query.all())


@app.route("/threads/new/")
@login_required
def threads_form():
    return render_template("threads/newthread.html", form=ThreadForm())


@app.route("/threads/", methods=["POST"])
@login_required
def threads_create():
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/newthread.html", form=ThreadForm())

    t = Thread(form.header.data)

    db.session().add(t)
    db.session().commit()

    p = Post(form.content.data)
    p.account_id = current_user.id
    p.thread_id = Thread.find_by_name(t.header)
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("threads_index"))
