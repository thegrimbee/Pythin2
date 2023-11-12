from flask import Blueprint, render_template
import pymongo
from . import user_bp

@user_bp.route('/login')
def login():
    print("Login page being rendered...")
    return render_template('login.html')

@user_bp.route('/register')
def register():
    print("Register page being rendered...")
    return render_template('register.html')
