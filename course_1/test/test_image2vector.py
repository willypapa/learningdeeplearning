import unittest

import numpy as np

from course_1.src import image2vector


class Image2VectorTest(unittest.TestCase):

    def test_image2vector(self):
        x = np.array([[[0.67826139, 0.29380381], [0.90714982, 0.52835647], [0.4215251, 0.45017551]],
                      [[0.92814219, 0.96677647], [0.85304703, 0.52351845], [0.19981397, 0.27417313]],
                      [[0.60659855, 0.00533165], [0.10820313, 0.49978937], [0.34144279, 0.94630077]]])

        expected = np.array([[0.67826139], [0.29380381], [0.90714982], [0.52835647], [0.4215251], [0.45017551],
                             [0.92814219], [0.96677647], [0.85304703], [0.52351845], [0.19981397], [0.27417313],
                             [0.60659855], [0.00533165], [0.10820313], [0.49978937], [0.34144279], [0.94630077]])

        self.assertTrue(np.allclose(image2vector.image2vector(x), expected))


if __name__ == '__main__':
    unittest.main()
