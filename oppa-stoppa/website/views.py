from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user


views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home.html')
def home():
    return render_template("home.html")

@views.route('/about.html')
def about():
    return render_template("about.html")

@views.route('/contactUs.html')
def contactUs():
    return render_template("contactUs.html")

@views.route('/about.html')
def about():
    return render_template("about.html")

@views.route('/forum.html')
def forum():
    return render_template('forum.html')

@views.route('/co_ops.html')
@login_required
def co_ops():
    return render_template('co_ops.html')

@views.route('/posts.html')
def posts():
    return render_template('posts.html')

@views.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@views.route('/help.html')
def help():
    return render_template("help.html")