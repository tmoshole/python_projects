import unittest
from io import StringIO
import sys
from test_base import captured_io
from unittest.mock import patch
import world.text.world


class MyTestCase(unittest.TestCase):
    def test_show_position(self):
        """
        Tests the function that moves the robot forward.
        """
        with patch('sys.stdout', new = StringIO()) as fakeout:
            world.text.world.show_position("HAL")
            self.assertEqual(fakeout.getvalue(), ' > HAL now at position (0,0).\n')


    def test_is_position_allowed(self):
        result = world.text.world.is_position_allowed(4,12)
        self.assertEqual(True, result)


    @patch("world.obstacles.obstacles_list",[(4,4), (14,5), (-15,35)])
    def test_position_blocked(self):
        results = world.text.world.is_position_allowed(4,12)
        self.assertEqual(True, results)


    @patch('world.text.world.position_x', 0)
    @patch('world.text.world.position_y', 0)
    @patch('world.text.world.current_direction_index', 0)
    @patch("world.obstacles.obstacles_list",[(4,0), (14,5), (-15,35)])
    def test_update_position(self):
        results = world.text.world.update_position(50)
        self.assertEqual(True, results)


    @patch('world.text.world.position_x', 0)
    @patch('world.text.world.position_y', 0)
    @patch('world.text.world.current_direction_index', 0)
    @patch("world.obstacles.obstacles_list",[(0,4), (14,5), (-15,35)])
    def test_update_position_fail(self):
        results = world.text.world.update_position(50)
        self.assertEqual(False, results)
        

    


if __name__ == "__main__":
    unittest.main()