from unittest import TestCase
from problems.number_of_islands import num_islands


class TestNumberOfIslands(TestCase):

    def test_none(self):
        result = num_islands(None)
        self.assertEqual(result, 0)

    def test_empty_1(self):
        result = num_islands([])
        self.assertEqual(result, 0)

    def test_empty_2(self):
        result = num_islands([[]])
        self.assertEqual(result, 0)

    def test_one_water(self):
        result = num_islands([
            [0]
        ])
        self.assertEqual(result, 0)

    def test_one_land(self):
        result = num_islands([
            [1]
        ])
        self.assertEqual(result, 1)

    def test_one_row(self):
        result = num_islands([
            [1, 0, 1]
        ])
        self.assertEqual(result, 2)

    def test_one_column(self):
        result = num_islands([
            [1],
            [0],
            [1]]
        )
        self.assertEqual(result, 2)

    def test_two_rows_1(self):
        result = num_islands([
            [1, 0, 1],
            [0, 1, 0]
        ])
        self.assertEqual(result, 3)

    def test_two_rows_2(self):
        result = num_islands([
            [1, 0, 1],
            [1, 1, 0]
        ])
        self.assertEqual(result, 2)

    def test_given_1(self):
        result = num_islands([
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.assertEqual(result, 1)

    def test_given_2(self):
        result = num_islands([
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ])
        self.assertEqual(result, 3)
