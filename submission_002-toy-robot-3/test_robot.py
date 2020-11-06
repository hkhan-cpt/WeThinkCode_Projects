#Steps 1-6: Create unit tests 
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

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nreplay\noff\n"))
    def test_replay(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,35).
 > Voltron moved forward by 5 steps.
 > Voltron now at position (0,40).
 > Voltron replayed 2 commands.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nreplay\nreplay\noff\n"))
    def test_replay_twice(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,35).
 > Voltron moved forward by 5 steps.
 > Voltron now at position (0,40).
 > Voltron replayed 2 commands.
 > Voltron now at position (0,40).
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,55).
 > Voltron moved forward by 5 steps.
 > Voltron now at position (0,60).
 > Voltron replayed 2 commands.
 > Voltron now at position (0,60).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nreplay silent\noff\n"))
    def test_replay_silent(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next?  > Voltron replayed 2 commands silently.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nreplay silent please\nreplay silent\noff\n"))
    def test_replay_silent_not_valid(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next? Voltron: Sorry, I did not understand 'replay silent please'.
Voltron: What must I do next?  > Voltron replayed 2 commands silently.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nREPLAY SILENT\noff\n"))
    def test_replay_silent_uppercase(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next?  > Voltron replayed 2 commands silently.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nreplay reversed\noff\n"))
    def test_replay_reversed(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,25).
 > Voltron moved forward by 15 steps.
 > Voltron now at position (0,40).
 > Voltron replayed 2 commands in reverse.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nreplay reverse\nreplay reversed\noff\n"))
    def test_replay_reversed_not_valid(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next? Voltron: Sorry, I did not understand 'replay reverse'.
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,25).
 > Voltron moved forward by 15 steps.
 > Voltron now at position (0,40).
 > Voltron replayed 2 commands in reverse.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nREPLAY REVERSED\noff\n"))
    def test_replay_reversed_uppercase(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,25).
 > Voltron moved forward by 15 steps.
 > Voltron now at position (0,40).
 > Voltron replayed 2 commands in reverse.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next?  > Voltron replayed 2 commands in reverse silently.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nREPLAY REVERSED SILENT\noff\n"))
    def test_replay_reversed_silent_uppercase(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next?  > Voltron replayed 2 commands in reverse silently.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nforward 5\nreplay reverse silent\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent_not_valid(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (0,20).
Voltron: What must I do next? Voltron: Sorry, I did not understand 'replay reverse silent'.
Voltron: What must I do next?  > Voltron replayed 2 commands in reverse silently.
 > Voltron now at position (0,40).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nright\nforward 5\nreplay 2\noff\n"))
    def test_replay_selection(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (5,15).
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (5,15).
 > Voltron moved forward by 5 steps.
 > Voltron now at position (5,10).
 > Voltron replayed 2 commands.
 > Voltron now at position (5,10).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nright\nforward 5\nreplay 2.5\nreplay 2\noff\n"))
    def test_replay_selection_not_valid(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (5,15).
Voltron: What must I do next? Voltron: Sorry, I did not understand 'replay 2.5'.
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (5,15).
 > Voltron moved forward by 5 steps.
 > Voltron now at position (5,10).
 > Voltron replayed 2 commands.
 > Voltron now at position (5,10).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nright\nforward 5\nreplay 3-1\noff\n"))
    def test_replay_selection_range(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (5,15).
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (20,15).
 > Voltron turned right.
 > Voltron now at position (20,15).
 > Voltron replayed 2 commands.
 > Voltron now at position (20,15).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nright\nforward 5\nreplay 3--1\nreplay 3-1\noff\n"))
    def test_replay_selection_range_not_valid(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (5,15).
Voltron: What must I do next? Voltron: Sorry, I did not understand 'replay 3--1'.
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (20,15).
 > Voltron turned right.
 > Voltron now at position (20,15).
 > Voltron replayed 2 commands.
 > Voltron now at position (20,15).
Voltron: What must I do next? Voltron: Shutting down..\n""")

    @patch("sys.stdin", StringIO("Voltron\nforward 15\nright\nforward 5\nreplay silent 2\noff\n"))
    def test_replay_selection_silent(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (5,15).
Voltron: What must I do next?  > Voltron replayed 2 commands silently.
 > Voltron now at position (5,10).
Voltron: What must I do next? Voltron: Shutting down..\n""")


    @patch("sys.stdin", StringIO("Voltron\nforward 15\nright\nforward 5\nreplay reversed 2\noff\n"))
    def test_replay_selection_reversed(self):
        sys.stdout = io.StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? Voltron: Hello kiddo!
Voltron: What must I do next?  > Voltron moved forward by 15 steps.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (0,15).
Voltron: What must I do next?  > Voltron moved forward by 5 steps.
 > Voltron now at position (5,15).
Voltron: What must I do next?  > Voltron turned right.
 > Voltron now at position (5,15).
 > Voltron moved forward by 15 steps.
 > Voltron now at position (5,0).
 > Voltron replayed 2 commands in reverse.
 > Voltron now at position (5,0).
Voltron: What must I do next? Voltron: Shutting down..\n""")


if __name__ == "__main__":
    unittest.main()