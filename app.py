import os

from flask import Flask, render_template, request

import utils
from utils import ALL_CANDIDATES

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()


@app.route('/')
def page_index():
    return render_template('index.html', data=ALL_CANDIDATES)


@app.route('/candidate_list/')
def page_list():
    candidates = {
        candidate["id"]: candidate["name"]
        for candidate in ALL_CANDIDATES
    }

    return render_template('candidate_list.html', data=candidates)


@app.route('/skill_list/')
def page_skill_list():
    skills = []
    candidates = [
        skills.extend(candidate["skills"].lower().split(", "))
        for candidate in ALL_CANDIDATES
    ]
    unique_skill_list = sorted(list(set(skills)))
    return render_template('skill_list.html', data=unique_skill_list)


@app.route('/candidate/<int:candidate_id>/')
def page_candidate_by_id(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    return render_template("card.html", data=candidate)


@app.route('/candidates/<skill_name>/')
def page_candidate_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("search_result.html", data=candidates)


@app.route('/search_result/', methods=['POST', 'GET'])
def page_search_result():
    candidate_name_or_skill = None
    if request.method == 'POST':
        candidate_name_or_skill = request.form['search']

    if not candidate_name_or_skill:
        candidates = [{"error": "Name or Skill of candidate is required"}]
    else:
        candidates = utils.get_candidates_by_name(candidate_name_or_skill)

    return render_template("search_result.html", data=candidates)


app.run(debug=True)
