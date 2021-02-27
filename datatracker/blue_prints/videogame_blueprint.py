from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests, json
from types import SimpleNamespace
from datatracker.blue_prints.invest_in import Invest
from datatracker.blue_prints.search import Search
bp = Blueprint('videogame_blueprint', __name__)

response = requests.get('https://api.dccresource.com/api/games')
games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
invest = Invest.invest_results(games)  # will not let me iterate over this
investing = invest                     # but I can iterate over this
new_search = Search.search_results(games)  # same as above, can't iterate over this
searching = new_search                     # but I can iterate over this one


@bp.route('/home')
def test():
    game_collection = []
    platform_collection = []
    global_sales = [get_sales("PS3"), get_sales("X360"), get_sales("3DS"), get_sales("PS4"), get_sales("XOne"),
                    get_sales("WiiU"), get_sales("Wii"), get_sales("PC"), get_sales("PSV"), get_sales("DS"),
                    get_sales("PSP")]

    # testg = len(games)  # test data - all games - returns 16598
    # testgc = len(game_collection)  # test data - games that have years -  returns 16327
    # testi = len(Invest.no_year(games)) # test data - prints to console all games that year is null - returns len 271

    for game in investing:  # this is appending only unique platforms to platform_collection list
        if game.platform not in platform_collection:
            platform_collection.append(game.platform)

    # print(platform_collection)  # for testing only. Will print consoles in platform_collection
    # test_tup = search_by_game_name("Super Mario Bros.")  # for testing only
    # print(tuple(test_tup))  # for testing only - returns (('NES', 40.24), ('GB', 5.07))
    return render_template('sample/index.html', x=platform_collection, y=global_sales)
    # 'sample/index.html refers to the folder then the .html'



def get_sales(platform):
    sales_total = 0
    for game in investing:
        if platform == game.platform:
            sales_total += game.globalSales
    return sales_total


@bp.route('/invest')  # see a data visualization of which video game console is best to invest in based on the number
                      # of game copies sold globally on that console since 2013
def invest():
    return " Time to invest"


@bp.route('/search', methods=('GET', 'POST'))  # be able to search for a game and see its details
def search_by_game_name():

    platform_list = []
    sales_list = []

    if request.method == 'POST':
        game_name = request.form['name']
        error = None
        for game in searching:
            if game.name == game_name:
                platform_list.append(game.platform)
                sales_list.append(game.globalSales)

        if not game_name:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        elif request.form['name'] == "go home":
            return redirect(url_for('sample.index'))
        else:
            return render_template('sample/index.html', x=platform_list, y=sales_list)

    else:
        return render_template('sample/index.html', page_title="PostForm from Module Function")


    # zipped_list = zip(platform_list, sales_list)  # creates a tuple of platform_list and sales_list

    #  return render_template('sample/index.html', )
    # 'sample/index.html refers to the folder then the .html'


@bp.route('/custom')  # custom search question
def custom_search():
    return " custom search please"

