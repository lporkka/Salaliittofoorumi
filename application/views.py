from flask import render_template, redirect, url_for
from application import app
from application.threads.models import Thread


@app.route("/")
def index():
    return redirect(url_for("threads_index"))
