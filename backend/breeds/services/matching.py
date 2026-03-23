from typing import Dict, List, TypedDict

from breeds.models import Breed


class MatchResult(TypedDict):
    breed: Breed
    score: float


WEIGHTS: Dict[str, float] = {
    "size": 1.0,
    "energy": 1.5,
    "kids": 2.0,
    "housing": 2.5,
}


def normalize_difference(value1: int, value2: int, max_value: int) -> float:
    return abs(value1 - value2) / max_value


def calculate_score(user_data: Dict, breed: Breed) -> float:
    score: float = 0.0

    # SIZE (1–3)
    score += WEIGHTS["size"] * normalize_difference(
        user_data["size"], breed.size, max_value=3
    )

    # ENERGY (1–5)
    score += WEIGHTS["energy"] * normalize_difference(
        user_data["energy"], breed.energy, max_value=5
    )

    # KIDS (1–5)
    score += WEIGHTS["kids"] * normalize_difference(
        user_data["kids"], breed.kids_friendly, max_value=5
    )

    # HOUSING (categorical parametrize)
    if breed.housing_type != user_data["housing"]:
        score += WEIGHTS["housing"]

    return score


def get_best_matches(
    user_data: Dict,
    breeds_queryset,
    limit: int = 5
) -> List[MatchResult]:

    results: List[MatchResult] = []

    for breed in breeds_queryset:
        score: float = calculate_score(user_data, breed)

        results.append({
            "breed": breed,
            "score": score
        })

    # sorted by score (lower = better)
    results.sort(key=lambda x: x["score"])

    return results[:limit]
