
from flask import Blueprint, render_template
from . import main_bp

@main_bp.route('/')
def index():
    print("Index page being rendered...")

    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')