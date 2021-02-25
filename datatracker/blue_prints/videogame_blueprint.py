from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests, json
from types import SimpleNamespace
from datatracker.blue_prints.invest_in import Invest

bp = Blueprint('videogame_blueprint', __name__)

response = requests.get('https://api.dccresource.com/api/games')
games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
invest = Invest.invest_results(games)

@bp.route('/home')
def test():

    invest_collection = []
    game_collection = []
    platform_collection = [] # create empty list for unique platforms
    for game in games:
        if str(game.year) != "None":
            game_collection.append(game)


    g = len(games)  # test data - all games - returns 16598
    gg = len(game_collection)  # test data - games that have years -  returns 16327

    print(games[0].platform)
    for game in game_collection: # this is appending only unique platforms to platform_collection list
        if game.platform not in platform_collection and game.year > 2012:
            platform_collection.append(game.platform)

    print(platform_collection)

    for game in games:
        if game.platform == "SAT":
            game_collection.append(game) # add game to list if platform is Wii and year 2007



    return render_template('sample/index.html', game_collection=game_collection, platform_collection=platform_collection)
    # 'sample/index.html refers to the folder then the .html'


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

