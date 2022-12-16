import os

from flask import Flask, render_template, request

import utils
from utils import ALL_CANDIDATES

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()


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


@app.route('/candidate/<int:candidate_id>/')
def page_candidate_by_id(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    return render_template("card.html", data=candidate)


@app.route('/search_result/', methods=['POST'])
def page_search_result():
    candidate_name = None

    if request.method == 'POST':
        candidate_name = request.form['search']

    if not candidate_name:
        candidates = [{"error": "Name of candidate is required"}]
    else:
        candidates = utils.get_candidates_by_name(candidate_name)

    return render_template("search_result.html", data=candidates)


app.run(debug=True)
