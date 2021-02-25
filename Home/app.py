from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/newest')
def chart():
labels: list[str] = ["Xbox","Playstation","wii","Playstation 2","Game cube","Nintendo 64","Saga Genesis","Atari"]
values = [10,9,8,7,6,4,7,8]
return render_template('chart.html', values=values, labels=labels)

if __name__ == "__main__":
app.run(host='0.0.0.0', port=5001)