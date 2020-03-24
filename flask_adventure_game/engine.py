import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('engine', __name__)

@bp.route('/', methods=('GET', 'POST'))
def game():

    return render_template('index.html', message='Welcome to Dungeon Escape!')
