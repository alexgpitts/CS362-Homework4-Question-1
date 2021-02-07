import unittest
import volume_of_a_cube

class TestCase(unittest.TestCase):

    #testing int values
    def test_volume_of_a_cube(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(4), 64)


    #testing if float nums work
    def test_volume_of_a_cube_float(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(4.0), 64.0)


    #testing if it can tell when negative values are entered for edge
    def test_negative_edge(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(-4), 64)



if __name__ == '__main__':
    unittest.main(verbosity=2)