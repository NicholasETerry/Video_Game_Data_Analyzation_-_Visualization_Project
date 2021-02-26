import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from datatracker.blue_prints import sample
    app.register_blueprint(sample.bp)
    from datatracker.blue_prints import videogame_blueprint  # for testing only , build factory
    app.register_blueprint(videogame_blueprint.bp)

    # app.add_url_rule('/', endpoint='index')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
