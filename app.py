import os

from flask import Flask, render_template, request

import utils
from utils import ALL_CANDIDATES

app = Flask(__name__)

# secret_key generation for flask session
# to get access to POST and GET methods
app.config['SECRET_KEY'] = os.urandom(24).hex()


@app.route('/')
def page_index():
    """
    Index page wit all candidates cards
    :return:  - render_template('index.html', data=ALL_CANDIDATES)
    """
    return render_template('index.html', data=ALL_CANDIDATES)


@app.route('/candidate_list/')
def page_list():
    """
    All candidate list page
    :return: - render_template('candidate_list.html', data=candidates)
    """
    return render_template('candidate_list.html', data=ALL_CANDIDATES)


@app.route('/skill_list/')
def page_skill_list():
    """
    All skills list page
    :return: - render_template('skill_list.html', data=skill_list)
    """
    skill_list = utils.get_skills_list()
    return render_template('skill_list.html', data=skill_list)


@app.route('/candidate/<int:candidate_id>/')
def page_candidate_by_id(candidate_id):
    """
    Candidate personal page/card by id
    :param      - candidate_id: - candidate id
    :return:    - render_template("card.html", data=candidate)
    """
    candidate = utils.get_candidate(candidate_id)
    return render_template("card.html", data=candidate)


@app.route('/candidates/<skill_name>/')
def page_candidate_by_skill(skill_name):
    """
    All candidate list with specified skill name
    :param skill_name:  - specified skill name or part
    :return: - render_template("search_result.html", data=candidates)
    """
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('candidate_list.html', data=candidates)


@app.route('/search_result/', methods=['POST'])
def page_search_result():
    """
    Search result page
    :return: render_template("search_result.html", data=candidates)
    """
    by_skill_count = 0
    by_name_count = 0
    candidate_name_or_skill = None

    if request.method == 'POST':
        candidate_name_or_skill = request.form['search']

    if not candidate_name_or_skill:
        candidates_by_skill = candidates_by_name = [
            {"error": "Name or Skill of candidate is required"}
        ]
    else:
        candidates_by_skill = utils.get_candidates_by_skill(
            candidate_name_or_skill
        )

        candidates_by_name = utils.get_candidates_by_name(
            candidate_name_or_skill
        )

    try:
        candidates_by_name[0]['error']
    except KeyError:
        by_name_count = len(
            candidates_by_name
        )

    try:
        candidates_by_skill[0]['error']
    except KeyError:
        by_skill_count = len(
            candidates_by_skill
        )

    return render_template(
        "search_result.html",
        candidates_by_name=candidates_by_name,
        candidates_by_skill=candidates_by_skill,
        by_name_count=by_name_count,
        by_skill_count=by_skill_count
    )


if __name__ == "__main__":
    app.run(debug=True)
