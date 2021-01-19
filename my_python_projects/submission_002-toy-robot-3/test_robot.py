import unittest
import robot
import sys
from unittest.mock import patch
from io import StringIO
from test_base import captured_io

class test_robot(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\n"))
    def test_name_robot(self):
        """
        Tests the input name of the robot function.
        """
        with patch('sys.stdout', new = StringIO()) as fakeout:
           self.assertEqual(robot.get_robot_name(),"HAL")


    @patch("sys.stdin", StringIO("HELP\noff\n"))
    def test_game_commands(self):
        """
        Test the get command from the user.
        """
        with patch('sys.stdout', new = StringIO()) as fakeout:
            self.assertEqual(robot.get_command("HAL"),"help")

    
    def test_help_command(self):
        """
        Tests the return of the help funtion.
        """
        self.assertEqual(robot.do_help(),(True,"""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
"""))

    def test_show_position(self):
        """
        Tests the function that moves the robot forward.
        """
        with patch('sys.stdout', new = StringIO()) as fakeout:
            robot.show_position("HAL")
            self.assertEqual(fakeout.getvalue(), ' > HAL now at position (0,30).\n')
    

    @patch("sys.stdin",StringIO("HAL\nforward 10\noff\n"))
    def test_do_forward(self):
        """
        testing the move forward funtion.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
        self.assertEqual(fakeout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..
""")
    
    @patch("sys.stdin",StringIO("HAL\nback 10\noff\n"))
    def test_do_back(self):
        """
        testing the move back function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
        self.assertEqual(fakeout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..
""")


    @patch("sys.stdin",StringIO("HAL\nright\noff\n"))
    def test_do_right_turn(self):
        """
        testing the turn right function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
        self.assertEqual(fakeout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin",StringIO("HAL\nleft\noff\n"))
    def test_do_left_turn(self):
        """
        testing the turn left function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
        self.assertEqual(fakeout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""")


    @patch("sys.stdin",StringIO("HAL\nforward 5\nforward 10\nreplay\noff\n"))
    def test_replay_commands(self):
        """
        testing the funtion that replays the movements commands given by the player
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
            results = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,20).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..
"""
            self.assertEqual(fakeout.getvalue(), results)


    
    @patch("sys.stdin",StringIO("HAL\nforward 20\nback 5\nreplay silent\noff\n"))
    def test_replay_silent(self):
        """
        testing the replay silent function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
            results = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL moved back by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..
"""
            self.assertEqual(fakeout.getvalue(), results)


    @patch("sys.stdin",StringIO("HAL\nforward 20\nback 5\nreplay reversed\noff\n"))
    def test_do_replay_reversed(self):
        """
        testing the replay reversed function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
            results = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL moved back by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved back by 5 steps.
 > HAL now at position (0,10).
 > HAL moved forward by 20 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..
"""
            self.assertEqual(fakeout.getvalue(),results)

    @patch("sys.stdin",StringIO("HAL\nforward 20\nback 5\nreplay reversed silent\noff\n"))
    def test_do_replay_reversed_silent(self):
        """
        testing the replay revsersed silently function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
            results = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL moved back by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..
"""
            self.assertEqual(fakeout.getvalue(),results)

    
    @patch("sys.stdin",StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 2\noff\n'))
    def test_replay_limit_range(self):
        """
        testing the replay limit range function
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
            results = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,8).
 > HAL moved forward by 1 steps.
 > HAL now at position (0,9).
 > HAL replayed 2 commands.
 > HAL now at position (0,9).
HAL: What must I do next? HAL: Shutting down..
"""
            self.assertEqual(fakeout.getvalue(),results)

    
    @patch("sys.stdin",StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 2-1\noff\n'))
    def test_replay_limit_parameters(self):
        """
        testing the replay limit parameters function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
            self.assertEqual(fakeout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,8).
 > HAL replayed 1 commands.
 > HAL now at position (0,8).
HAL: What must I do next? HAL: Shutting down..
""")


    @patch("sys.stdin",StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 2 silent\noff\n'))
    def test_do_replay_limit_range_silent(self):
        """
        testing the replay limit range silently function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
            self.assertEqual(fakeout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (0,9).
HAL: What must I do next? HAL: Shutting down..
""")


    @patch("sys.stdin",StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 2 reversed\noff\n'))
    def test_do_replay_limit_reversed(self):
        """
        testing the replay limit reversed function.
        """
        with patch("sys.stdout",new=StringIO()) as fakeout:
            robot.robot_start()
            self.assertEqual(fakeout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,8).
 > HAL moved forward by 3 steps.
 > HAL now at position (0,11).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..
""")


if __name__ == "__main__":
    unittest.main()