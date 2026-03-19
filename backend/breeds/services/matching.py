def calculate_score(user_data, breed):
    score = 0

    score += abs(user_data["size"] - breed.size)

    score += abs(user_data["energy"] - breed.energy)

    score += abs(user_data["kids"] - breed.kids_friendly)

    if breed.housing_type != user_data["housing"]:
        score += 2

    return score


def get_best_matches(user_data, breeds_queryset, limit=5):

    results = []

    for breed in breeds_queryset:
        score = calculate_score(user_data, breed)

        results.append({
            "breed": breed,
            "score": score
        })

    results.sort(key=lambda x: x["score"])

    return results[:limit]
