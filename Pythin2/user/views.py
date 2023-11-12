from flask import Blueprint, render_template, request, redirect, url_for
from ..database.db import user_db
from . import user_bp

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("Login page being rendered...")
        username = request.form['username']
        password = request.form['password']
        if user_db.login_user(username, password):
            print(f"{username} logged in")
            return redirect(url_for('index'))
        else:
            print("Login failed")
            return render_template('login.html')
    else :
        print("Login page being rendered...")
        return render_template('login.html')

@user_bp.route('/register')
def register():
    print("Register page being rendered...")
    return render_template('register.html')