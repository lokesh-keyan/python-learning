import unittest
from leetcode.array_and_hashing.contains_duplicate import Solution as ContainsDuplicateSolution
from leetcode.array_and_hashing.valid_anagram import Solution as IsAnagramSolution

class TestArrayAndHashing(unittest.TestCase):

    def setUp(self):
        self.contains_duplicate_test_cases = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
        ]

        self.is_anagram_test_cases = [
            ("anagram", "nagaram", True),
            ("rat", "car", False),
            ("a", "b", False)
        ]


    def test_contains_duplicate(self):
        contains_duplicate_solution = ContainsDuplicateSolution()
        for nums, expected in self.contains_duplicate_test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(
                    contains_duplicate_solution.contains_duplicate(nums),
                    expected
                )

    def test_is_anagram(self):
        is_anagram_solution = IsAnagramSolution()
        for s, t, expected in self.is_anagram_test_cases:
            with self.subTest(s=s, t=t, expected=expected):
                self.assertEqual(
                    is_anagram_solution.is_anagram(s, t),
                    expected
                )
    
if __name__ == "__main__":
    unittest.main()
        
