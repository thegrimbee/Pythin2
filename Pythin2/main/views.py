
from flask import Blueprint, render_template

homepage_bp = Blueprint('homepage_bp', __name__)

@homepage_bp.route('/')
def index():
    return render_template('index.html')


