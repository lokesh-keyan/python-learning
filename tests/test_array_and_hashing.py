import unittest
from leetcode.array_and_hashing import contains_duplicate

class TestArrayAndHashing(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
        ]

    def test_contains_duplicate(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(contains_duplicate(nums), expected)
