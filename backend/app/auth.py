from flask import Blueprint, render_template, redirect,url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Username address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))