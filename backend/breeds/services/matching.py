from typing import Dict, List, TypedDict

from breeds.models import Breed


class MatchResult(TypedDict):
    breed: Breed
    score: float
    match: float


WEIGHTS: Dict[str, float] = {
    "size": 1.0,
    "energy": 1.5,
    "kids": 2.0,
    "housing": 2.5,
}


def normalize_difference(value1: int, value2: int, max_value: int) -> float:
    return abs(value1 - value2) / max_value


def housing_match(user_value: str, breed_value: str) -> float:
    """
    Returns 0 if it matches perfectly
    and 1 if it does not match
    """

    if breed_value == Breed.HousingType.BOTH:
        return 0.0

    if user_value == breed_value:
        return 0.0

    return 1.0


def calculate_score(user_data: Dict, breed: Breed) -> float:
    score: float = 0.0

    # SIZE (1–3)
    score += WEIGHTS["size"] * normalize_difference(
        user_data["size"],
        breed.size,
        max_value=3
    )

    # ENERGY (1–5)
    score += WEIGHTS["energy"] * normalize_difference(
        user_data["energy"],
        breed.energy,
        max_value=5
    )

    # KIDS (1–5)
    score += WEIGHTS["kids"] * normalize_difference(
        user_data["kids"],
        breed.kids_friendly,
        max_value=5
    )

    # HOUSING (categorical)
    score += WEIGHTS["housing"] * housing_match(
        user_data["housing_type"],
        breed.housing_type
    )

    return score


def calculate_match_percentage(score: float) -> float:
    """
    Convert the score to a percentage (0–100%)
    The lower the score, the better
    """

    max_score = sum(WEIGHTS.values())

    normalized = score / max_score

    match = (1 - normalized) * 100

    return round(match, 2)


def get_best_matches(
    user_data: Dict,
    breeds_queryset,
    limit: int = 5
) -> List[MatchResult]:

    results: List[MatchResult] = []

    for breed in breeds_queryset:
        score: float = calculate_score(user_data, breed)

        match_percent: float = calculate_match_percentage(score)

        results.append({
            "breed": breed,
            "score": round(score, 3),
            "match": match_percent,
        })

    results.sort(key=lambda x: x["score"])

    return results[:limit]