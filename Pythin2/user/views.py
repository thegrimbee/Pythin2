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
            return redirect(url_for('main.index'))
        else:
            print("Login failed")
            return render_template('user.html', type='login', failed=True)
    else:
        print("Login page being rendered...")
        return render_template('user.html', type='login', failed=False)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print("Registering user...")
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        if user_db.register_user(email, username, password):
            print(f"{username} registered")
            return redirect(url_for('main.index'))
        else:
            print("Registration failed")
            return render_template('user.html', type='register', failed=True)
    else:
        print("Register page being rendered...")
        return render_template('user.html', type='register', failed=False)
    
@user_bp.route('/verify/<code>')
def verify(code):
    print("Verifying user...")
    if user_db.verify_user(code):
        print("User verified")
        return redirect(url_for('main.index'))
    else:
        print("Verification failed")
        return redirect(url_for('main.index'))
