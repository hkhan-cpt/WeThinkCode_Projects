import unittest
import robot
import sys
import io
from io import StringIO
from unittest.mock import patch
from robot import *


class MyTestCase(unittest.TestCase):
    """Mocking was used for all the tests below to mimic input provided by the user. All tests are ended by shutting down
    the robot using the "off" command.  
    """
    def test_store_history(self):
        pass

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nreplay\noff\n"))
    def test_replay(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,35).
 > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,40).
 > VOLTRON replayed 2 commands.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nreplay\nreplay\noff\n"))
    def test_replay_twice(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,35).
 > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,40).
 > VOLTRON replayed 2 commands.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,55).
 > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,60).
 > VOLTRON replayed 2 commands.
 > VOLTRON now at position (0,60).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nreplay silent\noff\n"))
    def test_replay_silent(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next?  > VOLTRON replayed 2 commands silently.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nreplay silent please\nreplay silent\noff\n"))
    def test_replay_silent_not_valid(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next? VOLTRON: Sorry, I did not understand 'replay silent please'.
VOLTRON: What must I do next?  > VOLTRON replayed 2 commands silently.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nREPLAY SILENT\noff\n"))
    def test_replay_silent_uppercase(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next?  > VOLTRON replayed 2 commands silently.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nreplay reversed\noff\n"))
    def test_replay_reversed(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,25).
 > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,40).
 > VOLTRON replayed 2 commands in reverse.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nreplay reverse\nreplay reversed\noff\n"))
    def test_replay_reversed_not_valid(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next? VOLTRON: Sorry, I did not understand 'replay reverse'.
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,25).
 > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,40).
 > VOLTRON replayed 2 commands in reverse.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nREPLAY REVERSED\noff\n"))
    def test_replay_reversed_uppercase(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,25).
 > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,40).
 > VOLTRON replayed 2 commands in reverse.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next?  > VOLTRON replayed 2 commands in reverse silently.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nREPLAY REVERSED SILENT\noff\n"))
    def test_replay_reversed_silent_uppercase(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next?  > VOLTRON replayed 2 commands in reverse silently.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nforward 5\nreplay reverse silent\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent_not_valid(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (0,20).
VOLTRON: What must I do next? VOLTRON: Sorry, I did not understand 'replay reverse silent'.
VOLTRON: What must I do next?  > VOLTRON replayed 2 commands in reverse silently.
 > VOLTRON now at position (0,40).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nright\nforward 5\nreplay 2\noff\n"))
    def test_replay_selection(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (5,15).
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (5,15).
 > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (5,10).
 > VOLTRON replayed 2 commands.
 > VOLTRON now at position (5,10).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nright\nforward 5\nreplay 2.5\nreplay 2\noff\n"))
    def test_replay_selection_not_valid(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (5,15).
VOLTRON: What must I do next? VOLTRON: Sorry, I did not understand 'replay 2.5'.
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (5,15).
 > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (5,10).
 > VOLTRON replayed 2 commands.
 > VOLTRON now at position (5,10).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nright\nforward 5\nreplay 3-1\noff\n"))
    def test_replay_selection_range(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (5,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (20,15).
 > VOLTRON turned right.
 > VOLTRON now at position (20,15).
 > VOLTRON replayed 2 commands.
 > VOLTRON now at position (20,15).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nright\nforward 5\nreplay 3--1\nreplay 3-1\noff\n"))
    def test_replay_selection_range_not_valid(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (5,15).
VOLTRON: What must I do next? VOLTRON: Sorry, I did not understand 'replay 3--1'.
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (20,15).
 > VOLTRON turned right.
 > VOLTRON now at position (20,15).
 > VOLTRON replayed 2 commands.
 > VOLTRON now at position (20,15).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")

    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nright\nforward 5\nreplay silent 2\noff\n"))
    def test_replay_selection_silent(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (5,15).
VOLTRON: What must I do next?  > VOLTRON replayed 2 commands silently.
 > VOLTRON now at position (5,10).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")


    @patch("sys.stdin", StringIO("VOLTRON\nforward 15\nright\nforward 5\nreplay reversed 2\noff\n"))
    def test_replay_selection_reversed(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? VOLTRON: Hello kiddo!
VOLTRON: What must I do next?  > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (0,15).
VOLTRON: What must I do next?  > VOLTRON moved forward by 5 steps.
 > VOLTRON now at position (5,15).
VOLTRON: What must I do next?  > VOLTRON turned right.
 > VOLTRON now at position (5,15).
 > VOLTRON moved forward by 15 steps.
 > VOLTRON now at position (5,0).
 > VOLTRON replayed 2 commands in reverse.
 > VOLTRON now at position (5,0).
VOLTRON: What must I do next? VOLTRON: Shutting down..\n""")


if __name__ == "__main__":
    unittest.main()