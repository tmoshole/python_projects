import unittest
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests
from unittest.mock import patch
import world.obstacles as obstacles
import robot


class MyTestCase(unittest.TestCase):
    
    def test_obstacle_type(self):
        obstacles.obstacles = []
        results = obstacles.create_random_obstacles()
        if type(results) == list:
            type_results = True
        self.assertEqual(True, type_results)


    def test_lenght_list_obstacles(self):
        obstacles.obstacles_list = []
        obstacles_list = obstacles.create_random_obstacles()
        results = True
        if len(obstacles_list) > 10:
            results = False
        self.assertEqual(True, results)
    

    def test_create_obstacles(self):
        results = obstacles.create_random_obstacles()
        obstacles.obstacles = []
        obstacles.obstacles.append(results)
        self.assertIn(results, obstacles.obstacles)
        

    @patch("world.obstacles.obstacles_list",[(4,4), (14,5), (-15,35)])
    def test_obstacles_path_blocked(self):
        result = obstacles.is_path_blocked(4,12, 4,0)
        self.assertEqual(True, result)


    @patch("world.obstacles.obstacles_list",[(4,4), (14,5), (-15,35)])
    def test_obstacles_path_not_blocked(self):
        result = obstacles.is_path_blocked(4,12, 9,0)
        self.assertEqual(False, result)


    @patch("world.obstacles.obstacles_list",[(4,4), (14,5), (-15,35)])
    def test_position_blocked_true(self):
        results = obstacles.is_position_blocked(6,6)
        self.assertEqual(True, results)


    @patch("world.obstacles.obstacles_list",[(4,4), (14,5), (-15,35)])
    def test_position_blocked_false(self):
        results = obstacles.is_position_blocked(12,0)
        self.assertEqual(False, results)
        

if __name__ == '__main__':
    unittest.main()