def calculate_popularity(emotion, urgency, lexical, readability):
    score = (
        0.3 * emotion +
        0.3 * urgency +
        0.2 * lexical +
        0.2 * readability
    )
    return score