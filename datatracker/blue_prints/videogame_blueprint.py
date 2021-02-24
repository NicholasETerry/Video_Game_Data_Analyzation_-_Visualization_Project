from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint


bp = Blueprint('videogame_blueprint', __name__)


@bp.route('/home')
def test():
    return "All good on the Home Front"


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

