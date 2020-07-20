# https://leetcode.com/discuss/interview-question/542597/


def most_popular_keywords(reviews, keywords, k):
    # If we are missing a parameter, there is nothing to return.
    if not (reviews and keywords and k):
        return []

    # This is its own function because I don't know exactly what is expected.
    # Therefore, I want to be able to change it easily.
    def tokenize_review(review):
        # Assume splitting on space is enough as a first guess.
        return review.split(' ')

    keyword_counts = {keyword: 0 for keyword in keywords}

    # This is similar to what Elasticsearch would do when it "analyzes".
    analyzed_reviews = [
        set(tokenize_review(review.lower())) for review in reviews
    ]
    for analyzed_review in analyzed_reviews:
        for keyword in keywords:
            if keyword in analyzed_review:
                keyword_counts[keyword] += 1

    result = list(keyword_counts.items())

    # Sort by descending count but ascending keyword.
    result.sort(key=lambda x: (-x[1], x[0]))

    # Take the top k and only return the keyword itself, not the count.
    result = [item[0] for item in result[:k]]
    return result
