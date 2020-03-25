import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from flask_adventure_game.map import Map

bp = Blueprint('engine', __name__)

@bp.route('/', methods=('GET', 'POST'))
def game():

    if (request.method == 'POST'):

        map = Map()
        command = request.form['command']

        if 'north' in command:
            resp = make_response(render_template('index.html', message=map.next_room('north_room')))
            resp.set_cookie('current_room', 'north_room')
            print(resp.headers)
            return resp

    return render_template('index.html', message='Welcome to Dungeon Escape!')
