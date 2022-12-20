import json
import os

# path to json file
PATH = os.path.join("data", "person.json")


def load_candidates_from_json(path):
    """
    Get all candidates from json file
    :param path:    - path to json file
    :return:        - all candidates
    """
    with open(path, encoding='utf-8') as file:
        all_candidates = json.load(file)
    return all_candidates


# all candidates saved in CONSTANT in order
# to avoid multiple call for json file
ALL_CANDIDATES = load_candidates_from_json(PATH)


def get_candidate(candidate_id):
    """
    Get candidate by id
    :param candidate_id:    - candidate id
    :return:                - returns candidate
    """
    for candidate in ALL_CANDIDATES:
        if candidate["id"] == int(candidate_id):
            return candidate

    return {"error": f"Candidate #{candidate_id} is missing"}


def get_candidates_by_name(candidate_name):
    """
    Get candidate by name or part of name
    :param candidate_name:  - candidate name or part of name
    :return:                - list of candidates by specified name
    """
    return [
               candidate
               for candidate in ALL_CANDIDATES if
               candidate_name.lower().strip() in candidate["name"].lower()
           ] or [
               {
                   "error": f"Candidate {candidate_name} is missing"
               }
           ]


# todo: searching in skills string by part of skill name same as by_name
def get_candidates_by_skill(skill_name):
    """
    Get candidates by skill name
    :param skill_name:  - specified skill name
    :return:            - list of candidates by specified skill name
    """
    return [
               candidate
               for candidate in ALL_CANDIDATES if
               skill_name.lower().strip() in candidate["skills"].lower()
           ] or [
               {
                   "error": f"Candidate with {skill_name} skill is missing"
               }
           ]


def get_skills_list():
    """
    Get list of all skills
    :return: - uniq skills list
    """
    skills = []

    for candidate in ALL_CANDIDATES:
        skills.extend(candidate["skills"].lower().split(", "))

    unique_skill_list = sorted(list(set(skills)))

    return unique_skill_list
