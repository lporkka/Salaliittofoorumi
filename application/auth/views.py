from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data,
                                password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html",
                               form=form,
                               error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form=RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("registerform.html", form=form)

    u = User(form.givename.data, form.giveusername.data,
             form.givepassword.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/logout")
@login_required(False)
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/upgrade")
@login_required(False)
def upgrade_account():
    u = db.session.query(User).get(current_user.id)
    u.admin = True
    db.session().commit()
    return redirect(url_for("index"))