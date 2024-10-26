# much of the creation of this file can be referenced from videos in the playlist found at
# https://www.youtube.com/playlist?list=PLCC34OHNcOtqJBOLjXTd5xC0e-VD3siPn (Codemy)
# and from https://www.youtube.com/watch?v=dam0GPOAvVI&t=7074s (Tech with Tim)
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Post
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
import random
import string

auth = Blueprint('auth', __name__)

@auth.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")



@auth.route('/logout')
def logout():

    return"<p>Logout</p>"



@auth.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        Fname = request.form.get('Fname')
        Lname = request.form.get('Lname')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')
        
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
            return redirect(url_for('auth.register'))
        if not('drexel.edu' in email):
            flash('Email must contain \"drexel.edu\"', category='error')
        elif len(Fname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != confirmpassword:
            flash('Passwords do not match', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email = email, first_name = Fname, password = generate_password_hash(
            password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("register.html")
