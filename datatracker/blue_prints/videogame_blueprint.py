from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests, json
from types import SimpleNamespace
from datatracker.blue_prints.invest_in import Invest

bp = Blueprint('videogame_blueprint', __name__)

response = requests.get('https://api.dccresource.com/api/games')
games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
invest = Invest.invest_results(games)  # will not let me iterate over this
investing = invest                     # but I can iterate over this

@bp.route('/home')
def test():

    game_collection = []
    platform_collection = []
    global_sales = [get_sales("PS3"), get_sales("X360"), get_sales("3DS"), get_sales("PS4"), get_sales("XOne"),
                    get_sales("WiiU"), get_sales("Wii"), get_sales("PC"), get_sales("PSV"), get_sales("DS"), get_sales("PSP")]
    testg = len(games)  # test data - all games - returns 16598
    testgc = len(game_collection)  # test data - games that have years -  returns 16327

    for game in investing: # this is appending only unique platforms to platform_collection list
        if game.platform not in platform_collection:
            platform_collection.append(game.platform)

    print(platform_collection)

    return render_template('sample/index.html', platform_collection=platform_collection, global_sales=global_sales)
    # 'sample/index.html refers to the folder then the .html'
def get_sales(platform):
    sales_total = 0
    for game in investing:
        if platform == game.platform:
            sales_total += game.globalSales
    return sales_total
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

