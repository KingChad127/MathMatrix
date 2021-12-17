import unittest

from math_matrix import MathMatrix

mat1 = MathMatrix([[5, 8, 1], [4, 6, 6], [10, 7, 2]])
mat2 = MathMatrix([[5, 10], [3, 78], [24, 56], [1, 0], [4, 18]])
mat3 = MathMatrix([[5, 2], [4, 9], [10, -3]])
mat4 = MathMatrix([[-11, 0], [7, 1], [-6, -8]])
mat5 = MathMatrix([[6], [5], [1]])
mat6 = MathMatrix([[3, 10, 8]])
mat7 = MathMatrix([[5, 1], [3, 8]])
mat8 = MathMatrix([[5, 4, 3, 2, 1]])
mat9 = MathMatrix([[1, 2, 5, 0], [0, 3, 2, 65], [0, 0, 4, -8], [0, 0, 0, 2]])


class TestMathMatrix(unittest.TestCase):

    # test matrix 8

    def test_get_num_rows(self):
        self.assertEqual(mat1.get_num_rows(), 3)
        self.assertEqual(mat2.get_num_rows(), 5)

    def test_get_num_cols(self):
        self.assertEqual(mat1.get_num_cols(), 3)
        self.assertEqual(mat2.get_num_cols(), 2)

    def test_get_val(self):
        # test every value in matrix 1
        for i in range(mat1.get_num_rows()):
            for j in range(mat1.get_num_cols()):
                self.assertEqual(mat1.get_val(i, j), mat1.values[i][j])

        # test every value in matrix 2
        for i in range(mat2.get_num_rows()):
            for j in range(mat2.get_num_cols()):
                self.assertEqual(mat2.get_val(i, j), mat2.values[i][j])

    def test_equals(self):
        self.assertEqual(mat1, MathMatrix([[5, 8, 1], [4, 6, 6], [10, 7, 2]]))
        self.assertEqual(mat2, MathMatrix([[5, 10], [3, 78], [24, 56], [1, 0], [4, 18]]))

    def test_add(self):
        self.assertEqual(mat3.add(mat4), MathMatrix([[-6, 2], [11, 10], [4, -11]]))

    def test_subtract(self):
        self.assertEqual(mat3.subtract(mat4), MathMatrix([[16, 2], [-3, 8], [16, 5]]))

    def test_multiply(self):
        self.assertEqual(mat5.multiply(mat6), MathMatrix([[18, 60, 48], [15, 50, 40], [3, 10, 8]]))

    def test_get_scaled_matrix(self):
        self.assertEqual(mat7.get_scaled_matrix(2), MathMatrix([[10, 2], [6, 16]]))

    def test_get_transpose(self):
        self.assertEqual(mat8.get_transposed(), MathMatrix([[5], [4], [3], [2], [1]]))

    def test_is_upper_triangular(self):
        self.assertEqual(mat9.is_upper_triangular(), True)
