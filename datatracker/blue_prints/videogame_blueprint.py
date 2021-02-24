from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests, json
from types import SimpleNamespace


bp = Blueprint('videogame_blueprint', __name__)


@bp.route('/home')
def test():
    game_collection = [] # create empty list
    response = requests.get('https://api.dccresource.com/api/games')
    games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))

    for game in games:
        if game.platform == "Wii" and game.year == 2007:
            game_collection.append(game) # add game to list if platform is Wii and year 2007

    return render_template('sample/index.html', game_collection=game_collection)


@bp.route('/invest') # see a data visualization of which video game console is best to invest in based on the number
                     # of game copies sold globally on that console since 2013
def invest():
    return " Time to invest"


@bp.route('/search') # be able to search for a game and see its details
def search():
    return " search for a game"


@bp.route('/custom') # custom search question
def custom_search():
    return " custom search please"

