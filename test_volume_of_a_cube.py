import unittest
import volume_of_a_cube

class TestCase(unittest.TestCase):

    #testing int values
    def test_volume_of_a_cube1(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(1, 4, 4), 16)

    def test_volume_of_a_cube2(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(4, 1, 4), 16)

    def test_volume_of_a_cube3(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(4, 4, 1), 16)


    #testing if float nums work
    def test_volume_of_a_cube_float(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(4.0, 4.0, 4.0), 64.0)


    #testing if it can tell when negative values are entered for length width or hight
    #individually
    def test_negative_length_error(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(-1, 4, 4), -1)

    def test_negative_width_error(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(4, -1, 4), -2)
    
    def test_negative_hight_error(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(4, 4, -1), -4)


    #testing if it can tell when negative values are entered for length width or hight
    #in combination
    def test_negative_length_and_width_error(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(-1, -5, 4), -3)

    def test_negative_length_and_hight_error(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(-1, 4, -4), -5)
    
    def test_negative_width_and_hight_error(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(1, -5, -4), -6)
    
    def test_negative_all_error(self):
        self.assertEqual(volume_of_a_cube.volume_of_cube(-1, -5, -4), -7)



if __name__ == '__main__':
    unittest.main(verbosity=2)