from flask import Flask, Blueprint
from flask import Markup
from flask import Flask
from flask import render_template


bp = Blueprint('app', __name__)


@bp.route('/newest')
def chart():
    labels: list[str] = ["Xbox", "Playstation", "wii", "Playstation 2", "Game cube", "Nintendo 64", "Saga Genesis", "Atari"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels)

@bp.route('new')
def register_blueprint(bp):
    return
