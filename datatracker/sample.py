from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint

bp = Blueprint('sample', __name__)


@bp.route('/test')
def test():
    return "All good!"


@bp.route('/sample')
def index():
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('sample/index.html', message=message, word=phrase)


@app.route('/newest')
def chart():
labels: list[str] = ["Xbox","Playstation","wii","Playstation 2","Game cube","Nintendo 64","Saga Genesis","Atari"]
values = [10,9,8,7,6,4,7,8]
return render_template('chart.html', values=values, labels=labels)

if __name__ == "__main__":
app.run(host='0.0.0.0', port=5001)


@bp.route('/postform', methods=('GET', 'POST'))
def other_example():
    if request.method == 'POST':
        page_title = request.form['title']
        error = None

        if not page_title:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        elif request.form['title'] == "go home":
            return redirect(url_for('sample.index'))
        else:
            return render_template('sample/postform.html', page_title=page_title)

    else:
        return render_template('sample/postform.html', page_title="PostForm from Module Function")

