from flask import Flask, render_template

from utils import ALL_CANDIDATES

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html', data=ALL_CANDIDATES)


@app.route('/list/')
def page_list():
    candidates = {
        candidate["id"]: candidate["name"]
        for candidate in ALL_CANDIDATES
    }

    return render_template('list.html', data=candidates)


app.run(debug=True)
