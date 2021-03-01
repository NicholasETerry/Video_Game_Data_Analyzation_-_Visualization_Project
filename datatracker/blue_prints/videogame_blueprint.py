from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests, json
from types import SimpleNamespace
from datatracker.blue_prints.invest_in import Invest
from datatracker.blue_prints.search import Search
from datatracker.blue_prints.details import Details
bp = Blueprint('videogame_blueprint', __name__)

response = requests.get('https://api.dccresource.com/api/games') # if i have time, create a class to call this and below
games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
invest = Invest.invest_results(games)  # will not let me iterate over this
investing = invest                     # but I can iterate over this
new_search = Search.search_results(games)  # same as above, can't iterate over this
searching = new_search                     # but I can iterate over this one
usable = Details.usable_games(games)    # ''
game_collection = usable                # ''


@bp.route('/home', methods=("GET", "POST"))
def test():
    label = "Video Game Data"
    plt_col = []

    for game in investing:  # this is appending only unique platforms to platform_collection list
        if game.platform not in plt_col:
            plt_col.append(game.platform)

    global_sales = [get_sales(plt_col[0]), get_sales(plt_col[1]), get_sales(plt_col[2]), get_sales(plt_col[3]),
                    get_sales(plt_col[4]), get_sales(plt_col[5]), get_sales(plt_col[6]), get_sales(plt_col[7]),
                    get_sales(plt_col[8]), get_sales(plt_col[9]), get_sales(plt_col[10])]
    # test_g = len(games)  # test data - all games - returns 16598
    # test_gc = len(game_collection)  # test data - games that have years -  returns 16327
    # test_i = len(Invest.no_year(games)) # test data - prints to console all games that year is null - returns len 271
    # print(plt_col)  # for testing only. Will print consoles in platform_collection
    # test_tup = search_by_game_name("Super Mario Bros.")  # for testing only
    # print(tuple(test_tup))  # for testing only - returns (('NES', 40.24), ('GB', 5.07))
    return render_template('sample/index.html', x=plt_col, y=global_sales, label=label,)
    # 'sample/index.html refers to the folder then the .html'


def get_sales(platform):
    sales_total = 0
    for game in investing:
        if platform == game.platform:
            sales_total += game.globalSales
    return sales_total


@bp.route('/search', methods=('GET', 'POST'))
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

        label = game_name + ": Global Sales / Platform"
        if not game_name:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        else:
            return render_template('sample/search.html', x=platform_list, y=sales_list, lable=label)

    else:
        return render_template('sample/search.html', page_title="PostForm from Module Function")

    # zipped_list = zip(platform_list, sales_list)  # creates a tuple of platform_list and sales_list
    #  return render_template('sample/index.html', )
    # 'sample/index.html refers to the folder then the .html'


@bp.route('/details', methods=("GET", "POST"))
def get_details_of_game():
    game_return = []
    if request.method == 'POST':
        game_detail = request.form['game']
        error = None
        for game in game_collection:
            if game.name == game_detail:
                print(game)
                game_return.append(game)  # returns the attributes of a game but needs cleaning up

        label = game_detail + ": Global Sales / Platform"
        if not game_detail:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        else:
            return render_template('sample/details.html', game=game_detail, game_return=game_return, label=label)

    else:
        return render_template('sample/details.html', page_title="PostForm from Module Function")


@bp.route('/custom', methods=("GET", "POST"))  # which genre is most popular per region
def custom_search():
    sales_territories = ["North America", "Europe", "Japan"]
    game_return = []

    if request.method == 'POST':
        custom = request.form['custom']
        error = None
        index_value = genre_finder().index(custom)
        pop_list = most_pop(genre_finder())[index_value]  # Im proud of this !!!!!
        label = custom
        if error is not None:
            flash(error)
        else:
            return render_template('sample/custom.html', y=pop_list, x=sales_territories, label=label)

    else:
        return render_template('sample/custom.html', page_title="PostForm from Module Function")


def genre_finder():
    genre_list = []
    for game in game_collection:
        if game.genre not in genre_list:
            genre_list.append(game.genre)
    return genre_list


def most_pop(list_of_genres):
    totals = [[] for genre in list_of_genres]
    north_america_sales = 0
    europe_sales = 0
    japan_sales = 0
    i = 0
    while i != len(list_of_genres) - 1:
        for game in game_collection:
            if list_of_genres[i] == game.genre:
                north_america_sales += game.naSales
                europe_sales += game.euSales
                japan_sales += game.jpSales
        totals[i].append(north_america_sales * 1.27979)  # North American population 579 million people
        totals[i].append(europe_sales * 1)  # europe population 741 million people
        totals[i].append(japan_sales * 5.88095)  # japan population 126 million people
        i += 1
    # print(totals) for testing only
    return totals
