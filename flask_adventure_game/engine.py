import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from flask_adventure_game.map import Map
from flask_adventure_game.lexicon import scan

bp = Blueprint('engine', __name__)

@bp.route('/', methods=('GET', 'POST'))
def game():

    if (request.method == 'POST'):

        map = Map()
        command = scan(request.form['command'])
        location = request.cookies.get('current_room')
        if location == None:
            location = 'south_cell'

        if command['type'] == 'movement':

            destination = getattr(map, location).adjacent_rooms[command['detail']]

            if destination:

                resp = make_response(render_template('index.html', message=map.next_room(destination)))
                resp.set_cookie('current_room', destination)

                return resp


        resp = make_response(render_template('index.html', message=map.next_room(location)))
        resp.set_cookie('current_room', location)
        return resp

    return render_template('index.html', message='Welcome to Dungeon Escape!\nPress submit to continue...')

@bp.route('/reset', methods=['GET'])
def reset():

    resp = make_response(render_template('index.html', message='Welcome to Dungeon Escape!\nPress submit to continue...'))
    resp.set_cookie('current_room', 'south_cell')
    return resp
