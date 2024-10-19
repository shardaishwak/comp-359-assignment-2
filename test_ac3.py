import unittest
from algorithm.CSP import CSP
from algorithm.AC3 import AC3, makeArcQueue, remove_inconsistent_values
from collections import defaultdict

class TestAC3Algorithm(unittest.TestCase):
    def setUp(self):
        """Set up a simple CSP problem for testing."""
        variables = ['A', 'B', 'C']
        
        adjList = {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A']
        }

        domains = {
            'A': {1, 2, 3},
            'B': {1, 2},
            'C': {2, 3}
        }

        self.csp = CSP(variables=variables, adjList=adjList, domains=domains)

    def test_ac3_success(self):
        """Test if AC3 successfully makes the CSP arc-consistent."""
        queue = makeArcQueue(self.csp)
        result = AC3(self.csp, queue)
        self.assertTrue(result)
        self.assertEqual(self.csp.domains['A'], {1, 2, 3})
        self.assertEqual(self.csp.domains['B'], {1, 2})
        self.assertEqual(self.csp.domains['C'], {2, 3})

    def test_ac3_failure(self):
        """Test if AC3 fails when a domain becomes empty."""
        self.csp.domains['A'] = {1}
        self.csp.domains['B'] = {1}
        queue = makeArcQueue(self.csp)
        result = AC3(self.csp, queue)
        self.assertFalse(result) 

    def test_remove_inconsistent_values(self):
        """Test the remove_inconsistent_values function directly."""
        removals = defaultdict(set)
        revised = remove_inconsistent_values(self.csp, 'A', 'B', removals)
        self.assertFalse(revised)
        self.assertEqual(self.csp.domains['A'], {1, 2, 3})

    def test_makeArcQueue(self):
        """Test if the arc queue is correctly generated."""
        queue = makeArcQueue(self.csp)
        expected_arcs = [('A', 'B'), ('A', 'C'), ('B', 'A'), ('C', 'A')]
        self.assertCountEqual(queue, expected_arcs)

    def test_restore_domains(self):
        """Test restoring domains after values have been removed."""
        removals = defaultdict(set)
        remove_inconsistent_values(self.csp, 'A', 'B', removals)
        self.csp.restore_domains(removals)
        self.assertIn(1, self.csp.domains['A']) 

    def test_ac3_value_removal(self):
        """Test if AC3 removes inconsistent values when appropriate."""
        self.csp.domains['A'] = {1, 2}
        self.csp.domains['B'] = {1}
        queue = makeArcQueue(self.csp)
        result = AC3(self.csp, queue)
        self.assertTrue(result)
        self.assertEqual(self.csp.domains['A'], {2})
if __name__ == '__main__':
    unittest.main()