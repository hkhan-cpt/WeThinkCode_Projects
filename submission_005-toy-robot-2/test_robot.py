#Step 4: Create unit test 
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
    @patch("sys.stdin", StringIO("Jinzo\n"))
    def test_naming_robot(self):
        """Checks that the function returns the robot name provided by the user.
        """
        sys.stdout = io.StringIO()
        self.assertEqual(naming_robot(), """Jinzo""")


    def test_greet_user(self):
        """Checks that the function displays a welcome message to the user along with the robot name provided by the user.
        """
        sys.stdout = io.StringIO()
        greet_user("Jinzo")
        self.assertEqual(sys.stdout.getvalue(), """Jinzo: Hello kiddo!\n""" )


    @patch("sys.stdin", StringIO("dance\noff\n"))
    def test_incorrect_get_command_and_lowercase_off_command(self):
        """Checks the output for incorrect input provided by the user. Also checks the output when the user inputs a
        command using lowercase letters. 
        """
        sys.stdout = io.StringIO()
        get_command("Jinzo")
        off_command("Jinzo")
        self.assertEqual(sys.stdout.getvalue(), """Jinzo: What must I do next? Jinzo: Sorry, I did not understand 'dance'.
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("HELP\noff"))
    def test_correct_get_command_and_uppercase_help_command(self):
        """Checks the output for correct input provided by the user. Also checks the output when the user inputs a
        command using lowercase letters. Checks whether the valid commands are displayed correctly when the user uses
        the help command.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(), """Jinzo: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move the robot forward
BACK    - move the robot back
RIGHT   - make the robot do a right-turn
LEFT    - make the robot do a left-turn
SPRINT  - make the robot sprint forward
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("HeLp\noFf"))
    def test_correct_get_command_and_camelcase_help_command(self):
        """Checks the output for correct input provided by the user. Also checks the output when the user inputs a
        command using camelcase letters. Checks whether the valid commands are displayed correctly when the user uses
        the "help" command.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(), """Jinzo: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move the robot forward
BACK    - move the robot back
RIGHT   - make the robot do a right-turn
LEFT    - make the robot do a left-turn
SPRINT  - make the robot sprint forward
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("forward 15\noff\n"))
    def test_forward_command(self):
        """Checks that the robot moves forward according to the input provided by the user and that the y co-ordinate 
        updates correctly.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(),"""Jinzo: What must I do next?  > Jinzo moved forward by 15 steps.
 > Jinzo now at position (0,15).
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("back 25\noff\n"))
    def test_back_command(self):
        """Checks that the robot moves back according to the input provided by the user and that the y co-ordinate 
        updates correctly.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(),"""Jinzo: What must I do next?  > Jinzo moved back by 25 steps.
 > Jinzo now at position (0,-25).
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("right\nback 5\nright\nforward 10\nright\nback 3\noff\n"))
    def test_right_command(self):
        """"Checks that the robot successfully perfroms a right turn and moves forward and back in all directions
        according to the input provided by the user. Also checks that the x and y co-ordinates update correctly.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(),"""Jinzo: What must I do next?  > Jinzo turned right.
 > Jinzo now at position (0,0).
Jinzo: What must I do next?  > Jinzo moved back by 5 steps.
 > Jinzo now at position (-5,0).
Jinzo: What must I do next?  > Jinzo turned right.
 > Jinzo now at position (-5,0).
Jinzo: What must I do next?  > Jinzo moved forward by 10 steps.
 > Jinzo now at position (-5,-10).
Jinzo: What must I do next?  > Jinzo turned right.
 > Jinzo now at position (-5,-10).
Jinzo: What must I do next?  > Jinzo moved back by 3 steps.
 > Jinzo now at position (-2,-10).
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("left\nforward 10\nleft\nback 4\nleft \nforward 3\noff\n"))
    def test_left_command(self):
        """Checks that the robot successfully perfroms a left turn and moves forward and back in all directions
        according to the input provided by the user. Also checks that the x and y co-ordinates update correctly.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(),"""Jinzo: What must I do next?  > Jinzo turned left.
 > Jinzo now at position (0,0).
Jinzo: What must I do next?  > Jinzo moved forward by 10 steps.
 > Jinzo now at position (-10,0).
Jinzo: What must I do next?  > Jinzo turned left.
 > Jinzo now at position (-10,0).
Jinzo: What must I do next?  > Jinzo moved back by 4 steps.
 > Jinzo now at position (-10,4).
Jinzo: What must I do next?  > Jinzo turned left.
 > Jinzo now at position (-10,4).
Jinzo: What must I do next?  > Jinzo moved forward by 3 steps.
 > Jinzo now at position (-7,4).
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("forward 250\nforward 150\nforward 60\noff\n"))
    def test_fixed_area_y(self):
        """Checks that the robot can only move in the range -200 <= y <= 200. Also checks if the error message is diaplayed.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(),"""Jinzo: What must I do next? Jinzo: Sorry, I cannot go outside my safe zone.
 > Jinzo now at position (0,0).
Jinzo: What must I do next?  > Jinzo moved forward by 150 steps.
 > Jinzo now at position (0,150).
Jinzo: What must I do next? Jinzo: Sorry, I cannot go outside my safe zone.
 > Jinzo now at position (0,150).
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("left\nforward 150\nforward 50\nforward 60\noff\n"))
    def test_fixed_area_x(self):
        """Checks that the robot can only move in the range -100 <= x <= 100. Also checks if the error message is diaplayed.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(),"""Jinzo: What must I do next?  > Jinzo turned left.
 > Jinzo now at position (0,0).
Jinzo: What must I do next? Jinzo: Sorry, I cannot go outside my safe zone.
 > Jinzo now at position (0,0).
Jinzo: What must I do next?  > Jinzo moved forward by 50 steps.
 > Jinzo now at position (-50,0).
Jinzo: What must I do next? Jinzo: Sorry, I cannot go outside my safe zone.
 > Jinzo now at position (-50,0).
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


    @patch("sys.stdin", StringIO("sprint 7\n sprint 40\noff\n"))
    def test_sprint_command_and_fixed_area_y(self):
        """Checks that the function displays one less step as the robot sprints. Checks whether the position is displayed
        when the number of steps reach zero. Checks that the robot does not sprint beyond the fixed area.
        """
        sys.stdout = io.StringIO()
        loop_commands("Jinzo")
        self.assertEqual(sys.stdout.getvalue(),"""Jinzo: What must I do next?  > Jinzo moved forward by 7 steps.
 > Jinzo moved forward by 6 steps.
 > Jinzo moved forward by 5 steps.
 > Jinzo moved forward by 4 steps.
 > Jinzo moved forward by 3 steps.
 > Jinzo moved forward by 2 steps.
 > Jinzo moved forward by 1 steps.
 > Jinzo now at position (0,28).
Jinzo: What must I do next?  > Jinzo moved forward by 40 steps.
 > Jinzo moved forward by 39 steps.
 > Jinzo moved forward by 38 steps.
 > Jinzo moved forward by 37 steps.
Jinzo: Sorry, I cannot go outside my safe zone.
 > Jinzo now at position (0,182).
Jinzo: What must I do next? Jinzo: Shutting down..\n""")


if __name__ == "__main__":
    unittest.main()