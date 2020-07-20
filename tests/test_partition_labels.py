from unittest import TestCase
from problems.partition_labels import get_partition_labels


class TestPartitionLabels(TestCase):

    def test_none(self):
        result = get_partition_labels(None)
        self.assertEqual(result, [])

    def test_empty(self):
        result = get_partition_labels('')
        self.assertEqual(result, [])

    def test_simple_1(self):
        result = get_partition_labels("a")
        self.assertEqual(result, [1])

    def test_simple_2(self):
        result = get_partition_labels("abc")
        self.assertEqual(result, [1, 1, 1])

    def test_simple_3(self):
        result = get_partition_labels("abbccc")
        self.assertEqual(result, [1, 2, 3])

    def test_simple_4(self):
        result = get_partition_labels("abbcccbba")
        self.assertEqual(result, [9])

    def test_simple_5(self):
        result = get_partition_labels("abbcccbb")
        self.assertEqual(result, [1, 7])

    def test_given(self):
        result = get_partition_labels("ababcbacadefegdehijhklij")
        self.assertEqual(result, [9, 7, 8])
