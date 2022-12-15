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
    for candidate in ALL_CANDIDATES:
        if candidate["id"] == candidate_id:
            return candidate
        else:
            return {"error": f"Candidate #{candidate_id} is missing"}


def get_candidates_by_name(candidate_name):
    filtered_candidates = {}
    for candidate in ALL_CANDIDATES:
        if candidate_name.lower() == candidate["name"].lower():
            filtered_candidates[candidate["id"]] = candidate["name"]
    if filtered_candidates is {}:
        filtered_candidates["error"] = f"Candidate {candidate_name} is missing"
    return filtered_candidates


def get_candidates_by_skill(skill_name):
    pass
