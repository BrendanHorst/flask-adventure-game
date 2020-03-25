import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_adventure_game.map import Map

bp = Blueprint('engine', __name__)

@bp.route('/', methods=('GET', 'POST'))
def game():

    if (request.method == 'POST'):

        map = Map()
        command = request.form['command']

        if 'north' in command:
            return render_template('index.html', message=map.next_room('north_room'))

    return render_template('index.html', message='Welcome to Dungeon Escape!')
