import unittest
from world import obstacles
import sys
import io
from io import StringIO


class MyTestCase(unittest.TestCase):

    def test_get_obstacles(self):
        sys.stdout = io.StringIO()
        block_list = obstacles.get_obstacles()

        self.assertIsInstance(block_list, list)
        self.assertIn(len(block_list), range(0, 11))


    def test_is_position_blocked(self):
        obstacles.block_list = [(12,95), (-5,85), (-121,-23)]

        self.assertTrue(obstacles.is_position_blocked(12,95))
        self.assertFalse(obstacles.is_position_blocked(23,-125))


    def test_is_path_blocked(self):
        obstacles.block_list = [(12,95), (-5,85), (-121,-23)]

        self.assertTrue(obstacles.is_path_blocked(12,54, 12, 97))
        self.assertFalse(obstacles.is_path_blocked(23,-23, 23, -125))


if __name__ == "__main__":
    unittest.main()
