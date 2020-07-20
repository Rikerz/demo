from unittest import TestCase
from top_k_frequent_keywords import most_popular_keywords


class TestTopKFrequentKeywords(TestCase):

    def test_none(self):
        result = most_popular_keywords(None, None, None)
        self.assertEqual(result, [])

    def test_empty(self):
        result = most_popular_keywords([], [], 0)
        self.assertEqual(result, [])

    def test_simple_1(self):
        k = 1
        keywords = ["a", "b", "c"]
        reviews = ["a"] * 3 + ["b"] * 2 + ["c"] + ["d"] * 4
        result = most_popular_keywords(reviews, keywords, k)
        self.assertEqual(result, ["a"])

    def test_simple_2(self):
        k = 2
        keywords = ["a", "b", "c"]
        reviews = ["a"] * 3 + ["b"] * 2 + ["c"] + ["d"] * 4
        result = most_popular_keywords(reviews, keywords, k)
        self.assertEqual(result, ["a", "b"])

    def test_simple_3(self):
        k = 3
        keywords = ["a", "b", "c"]
        reviews = ["a"] * 3 + ["b"] * 2 + ["c"] + ["d"] * 4
        result = most_popular_keywords(reviews, keywords, k)
        self.assertEqual(result, ["a", "b", "c"])

    def test_simple_4(self):
        k = 4
        keywords = ["a", "b", "c"]
        reviews = ["a"] * 3 + ["b"] * 2 + ["c"] + ["d"] * 4
        result = most_popular_keywords(reviews, keywords, k)
        self.assertEqual(result, ["a", "b", "c"])

    def test_given_1(self):
        k = 2
        keywords = ["anacell", "cetracular", "betacellular"]
        reviews = [
            "Anacell provides the best services in the city",
            "betacellular has awesome services",
            "Best services provided by anacell, everyone should use anacell",
        ]
        result = most_popular_keywords(reviews, keywords, k)
        self.assertEqual(result, ["anacell", "betacellular"])

    def test_given_2(self):
        k = 2
        keywords = [
            "anacell",
            "betacellular",
            "cetracular",
            "deltacellular",
            "eurocell"
        ]
        reviews = [
            "I love anacell Best services; Best services provided by anacell",
            "betacellular has great services",
            "deltacellular provides much better services than betacellular",
            "cetracular is worse than anacell",
            "Betacellular is better than deltacellular.",
        ]
        result = most_popular_keywords(reviews, keywords, k)
        self.assertEqual(result, ["betacellular", "anacell"])
