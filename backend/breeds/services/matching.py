from typing import Dict, List, TypedDict

from breeds.models import Breed


class MatchResult(TypedDict):
    breed: Breed
    score: float
    match: float
    details: Dict[str, float]


WEIGHTS: Dict[str, float] = {
    "size": 1.0,
    "energy": 1.5,
    "kids": 2.0,
    "housing": 2.5,
}

MAX_SCORE: float = sum(WEIGHTS.values())


def normalize_difference(value1: int, value2: int, max_value: int) -> float:
    if max_value == 0:
        return 0.0
    return abs(value1 - value2) / max_value


def housing_match(user_value: str, breed_value: str) -> float:
    """
    0.0 — perfect
    0.5 — acceptable (minor penalty)
    """

    if breed_value == Breed.HousingType.BOTH:
        return 0.0

    if user_value == breed_value:
        return 0.0

    return 0.5


def calculate_score(user_data: Dict, breed: Breed):
    score: float = 0.0
    details: Dict[str, float] = {}

    # SIZE (1–3)
    size_diff = normalize_difference(user_data["size"], breed.size, 3)
    size_score = WEIGHTS["size"] * size_diff
    score += size_score
    details["size"] = round((1 - size_diff) * 100, 2)

    # ENERGY (1–5)
    energy_diff = normalize_difference(user_data["energy"], breed.energy, 5)
    energy_score = WEIGHTS["energy"] * energy_diff
    score += energy_score
    details["energy"] = round((1 - energy_diff) * 100, 2)

    # KIDS (1–5)
    kids_diff = normalize_difference(user_data["kids"], breed.kids_friendly, 5)
    kids_score = WEIGHTS["kids"] * kids_diff
    score += kids_score
    details["kids"] = round((1 - kids_diff) * 100, 2)

    # HOUSING (categorical)
    housing_diff = housing_match(user_data["housing_type"], breed.housing_type)
    housing_score = WEIGHTS["housing"] * housing_diff
    score += housing_score
    details["housing"] = 100 if housing_diff == 0 else 50

    return score, details


def calculate_match_percentage(score: float) -> float:
    """
    Convert score to percentage (0–100%)
    The lower the score, the better
    """

    normalized = score / MAX_SCORE
    match = (1 - normalized) * 100

    return round(match, 2)


def get_best_matches(
    user_data: Dict,
    breeds_queryset,
    limit: int = 5
) -> List[MatchResult]:

    results: List[MatchResult] = []

    for breed in breeds_queryset:
        score, details = calculate_score(user_data, breed)

        match_percent = calculate_match_percentage(score)

        results.append({
            "breed": breed,
            "score": round(score, 3),
            "match": match_percent,
            "details": details,
        })

    results = sorted(results, key=lambda x: x["score"])

    return results[:limit]
