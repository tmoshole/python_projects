import unittest
import robot
from unittest.mock import patch
from io import StringIO

class test_robot(unittest.TestCase):

    @patch("sys.stdin", StringIO("HAL\n"))
    def test_name_robot(self):
        """
        Tests the input name of the robot function.
        """
        with patch('sys.stdout', new = StringIO()) as fakeout:
           self.assertEqual(robot.name_robot(),"HAL")


    @patch("sys.stdin", StringIO("HELP\noff\n"))
    def test_game_commands(self):
        """
        Test the get command from the user.
        """
        with patch('sys.stdout', new = StringIO()) as fakeout:
            self.assertEqual(robot.game_commands("tim",0,1,0,0),["off"]) 
    

    def test_help_command(self):
        """
        Tests the return of the help funtion.
        """
        self.assertEqual(robot.help_command(),['I can understand these commands:','OFF  - Shut down robot','HELP - provide information about commands','FORWARD - move forward by specified number of steps, e.g. FORWARD 10','BACK - move back by specified number of steps, e.g. back 20','RIGHT - For the robot to turn right','LEFT - For the robot to turn left','SPRINT'])
    
    def test_forward(self):
        """
        Tests the function that moves the robot forward.
        """

        with patch('sys.stdout', new = StringIO()) as fakeout:
            results = robot.move_forward("HAL",["Forward","10"],0, 0)
            self.assertEqual(fakeout.getvalue(), ' > HAL moved forward by 10 steps.\n')

    def test_back(self):

        """
        Tests the function that moves the robot backwards.
        """
        with patch('sys.stdout', new = StringIO()) as fakeout:
            results = robot.move_back("HAL",["back","10"],0, 0)
            self.assertEqual(fakeout.getvalue(), ' > HAL moved back by 10 steps.\n')
    





if __name__ == "__main__":
    unittest.main()