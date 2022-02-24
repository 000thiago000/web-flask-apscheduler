from os import abort
from flask import render_template, request, redirect, url_for, abort, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Task
from app import app, db


@app.before_request
def check_login():
    if request.endpoint.split('.')[0] == 'scheduler' and not current_user.is_authenticated:
        return abort(401)
    return None


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))

        login_user(user)
        flash('You were successfully logged in')
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/functions')
@login_required
def func():
    cols = ['name', 'func']
    data = Task.query.order_by(Task.id.asc()).all()
    result = [{col: getattr(d, col) for col in cols} for d in data]
    return jsonify(result)
