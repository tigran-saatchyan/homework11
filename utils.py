import json
import os

PATH = os.path.join("static", "person.json")


def load_candidates_from_json(path):
    with open(path, encoding='utf-8') as file:
        all_candidates = json.load(file)
    return all_candidates


ALL_CANDIDATES = load_candidates_from_json(PATH)


def list_of_candidates():
    return


def get_candidate(candidate_id):
    result = []
    for candidate in ALL_CANDIDATES:
        if candidate["id"] == int(candidate_id):
            result = candidate

    if not result:
        result.append({"error": f"Candidate #{candidate_id} is missing"})

    return result


def get_candidates_by_name(candidate_name):
    filter_by_name = []
    for candidate in ALL_CANDIDATES:
        if candidate_name.lower().strip() in candidate["name"].lower().split():
            filter_by_name.append(candidate)

    if not filter_by_name:
        filter_by_name.append(
            {
                "error": f"Candidate {candidate_name} is missing"
            }
        )
    return filter_by_name


def get_candidates_by_skill(skill_name):
    filter_by_skill = []
    for candidate in ALL_CANDIDATES:
        if skill_name.lower().strip() in candidate["skills"].lower().split():
            print(skill_name.lower())
            print(candidate["skills"].lower().split())
            filter_by_skill.append(candidate)

    if not filter_by_skill:
        filter_by_skill.append(
            {
                "error": f"Candidate with {skill_name} skill is missing"
            }
        )
    return filter_by_skill
