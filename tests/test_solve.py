import unittest

from hungarian.solve import AssignmentError, brute_force, solve


class CheckTest(unittest.TestCase):
    def test_empty_matrix(self):
        with self.assertRaises(AssignmentError):
            solve([])

    def test_not_square(self):
        with self.assertRaises(AssignmentError):
            solve([[1, 2, 3], [4, 5, 6]])


class SolveTest(unittest.TestCase):
    def test_single_cell(self):
        self.assertEqual(solve([[5]]), (5, [0]))

    def test_diagonal_is_obvious(self):
        total, order = solve([[1, 9], [9, 1]])
        self.assertEqual((total, sorted(order)), (2, [0, 1]))

    def test_is_a_permutation(self):
        total, order = solve([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
        self.assertEqual(sorted(order), [0, 1, 2])

    def test_brute_force_matches_small_case(self):
        matrix = [[4, 1, 3], [2, 0, 5], [3, 2, 2]]
        best, _ = brute_force(matrix)
        self.assertEqual(best, 5)


if __name__ == "__main__":
    unittest.main()
