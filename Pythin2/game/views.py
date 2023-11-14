from flask import Blueprint, render_template
from .levels import *
from . import game_bp

@game_bp.route('/level<level>')
def play():
    return render_template('level.html', level=level)

