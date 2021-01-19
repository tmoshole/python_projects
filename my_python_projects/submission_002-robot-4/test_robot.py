import random
import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot
from unittest.mock import patch
import world.obstacles as obstacles

class MyTestClass(unittest.TestCase):
   
    def test_then_wrong_then_off(self):

        with captured_io(StringIO('HAL\ndance\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I did not understand 'dance'.
HAL: What must I do next? HAL: Shutting down..""", output)



    def test_sprint10_then_off(self):

        with captured_io(StringIO('HAL\nsprint 10\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL moved forward by 9 steps.
 > HAL moved forward by 8 steps.
 > HAL moved forward by 7 steps.
 > HAL moved forward by 6 steps.
 > HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.
 > HAL now at position (0,55).
HAL: What must I do next? HAL: Shutting down..""", output)


    def test_replay_basic(self):
        with captured_io(StringIO('HAL\nforward 20\nforward 10\nreplay\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,50).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,60).
 > HAL replayed 2 commands.
 > HAL now at position (0,60).
HAL: What must I do next? HAL: Shutting down..""", output)


    def test_replay_twice(self):
        with captured_io(StringIO('HAL\nforward 20\nforward 10\nreplay\nreplay\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,50).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,60).
 > HAL replayed 2 commands.
 > HAL now at position (0,60).
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,80).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,90).
 > HAL replayed 2 commands.
 > HAL now at position (0,90).
HAL: What must I do next? HAL: Shutting down..""", output)


    

if __name__ == '__main__':
    unittest.main()