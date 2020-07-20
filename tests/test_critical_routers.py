from unittest import TestCase
from critical_routers import find_critical_nodes


class TestCriticalRouters(TestCase):

    def test_none(self):
        result = find_critical_nodes(None, None, None)
        self.assertEqual(result, [])

    def test_empty(self):
        result = find_critical_nodes(0, 0, [])
        self.assertEqual(result, [])

    def test_simple_1(self):
        # Single node.
        num_nodes = 1
        num_edges = 0
        edges = []
        result = find_critical_nodes(num_nodes, num_edges, edges)
        self.assertEqual(result, [])

    def test_simple_2(self):
        # Two node line.
        num_nodes = 2
        num_edges = 1
        edges = [[0, 1]]
        result = find_critical_nodes(num_nodes, num_edges, edges)
        self.assertEqual(result, [])

    def test_simple_3(self):
        # Three node line.
        num_nodes = 3
        num_edges = 2
        edges = [[0, 1], [1, 2]]
        result = find_critical_nodes(num_nodes, num_edges, edges)
        self.assertEqual(result, [1])

    def test_simple_4(self):
        # Three node cycle.
        num_nodes = 3
        num_edges = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        result = find_critical_nodes(num_nodes, num_edges, edges)
        self.assertEqual(result, [])

    def test_simple_5(self):
        # Four node line.
        num_nodes = 4
        num_edges = 3
        edges = [[0, 1], [1, 2], [2, 3]]
        result = find_critical_nodes(num_nodes, num_edges, edges)
        self.assertEqual(result, [1, 2])

    def test_given(self):
        num_nodes = 7
        num_edges = 7
        edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
        result = find_critical_nodes(num_nodes, num_edges, edges)
        self.assertEqual(result, [2, 3, 5])
