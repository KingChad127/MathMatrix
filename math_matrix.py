from __future__ import annotations

import copy
from typing import List, Callable


class MathMatrix:
    def __init__(self, mat: List[List[int]]):
        # check preconditions
        if mat is None or len(mat) <= 0 or len(mat[0]) <= 0 or not self.__rectangular_matrix(mat):
            raise TypeError('Violation of preconditions')

        self.values = copy.deepcopy(mat)

    def __str__(self) -> str:
        """
        :return: a str representation of this matrix
        """
        # find the length of the longest integer
        longest_length = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                length = len(str(self.values[i][j]))
                if length > longest_length:
                    longest_length = length

        output = ''
        spaces = longest_length + 1
        str_format = '{:>' + str(spaces) + '}'
        for i in range(len(self.values)):
            output += '|'
            for j in range(len(self.values[i])):
                output += str_format.format(str(self.values[i][j]))

            output += ' |\n'

        return output

    def get_num_rows(self) -> int:
        """
        :return: the number of rows in this matrix
        """
        return len(self.values)

    def get_num_cols(self) -> int:
        """
        :return: the number of columns in this matrix
        """
        return len(self.values[0])

    def get_val(self, row: int, col: int) -> int:
        # check preconditions
        if not (0 <= row < len(self.values) or 0 <= row < len(self.values[0])):
            raise TypeError('Violation of preconditions: invalid row col')

        return self.values[row][col]

    def add(self, rhs: MathMatrix) -> MathMatrix:
        """
        Add two matrices together. self + rhs
        :param rhs: right-hand side MathMatrix
        :return: a new MathMatrix that is the result of self + rhs
        """
        return self.get_mat(rhs, lambda x, y: x + y)

    def subtract(self, rhs: MathMatrix) -> MathMatrix:
        """
        Subtract two matrices. self - rhs
        :param rhs: right-hand side MathMatrix
        :return: a new MathMatrix that is the result of self - rhs
        """
        return self.get_mat(rhs, lambda x, y: x - y)

    def get_mat(self, rhs: MathMatrix, operation: Callable[[int, int], int]) -> MathMatrix:
        """
        Perform an operation on the corresponding entries of two MathMatrices with the same
        dimensions
        :param rhs: right-hand side MathMatrix
        :param operation: the operation to complete
        :return: a new MathMatrix resulting from this operation
        """
        result = []
        if rhs is None or rhs.get_num_rows() != self.get_num_rows() or \
                rhs.get_num_cols() != self.get_num_cols():
            raise TypeError('Violation of Preconditions')

        for i in range(self.get_num_rows()):
            result.append([])
            for j in range(self.get_num_cols()):
                result[i].append(operation(self.values[i][j], rhs.values[i][j]))

        return MathMatrix(result)

    def multiply(self, rhs: MathMatrix) -> MathMatrix:
        """
        Multiply two matrices together if the dimensions permit
        :param rhs: right-hand side matrix
        :return: a new MathMatrix that is the result of multiplying self and rhs
        """
        if rhs is None or rhs.get_num_rows() != self.get_num_cols():
            raise TypeError('Matrix product does not exist')

        result_rows = self.get_num_rows()
        result_cols = rhs.get_num_cols()
        num_of_dp_ops = rhs.get_num_rows()
        result = []

        for i in range(result_rows):
            result.append([])
            for j in range(result_cols):
                val = 0
                for k in range(num_of_dp_ops):
                    val += self.get_val(i, k) * rhs.get_val(k, j)
                result[i].append(val)

        return MathMatrix(result)

    def get_scaled_matrix(self, factor: int) -> MathMatrix:
        """
        Multiply this matrix by a scalar
        :param factor: the scalar to multiply by
        :return: a new MathMatrix that is the scalar multiplied by self
        """
        scaled_rows = self.get_num_rows()
        scaled_cols = self.get_num_cols()
        result = []
        for i in range(scaled_rows):
            result.append([])
            for j in range(scaled_cols):
                result[i].append(factor * self.get_val(i, j))

        return MathMatrix(result)

    def get_transposed(self) -> MathMatrix:
        """
        Get a transpose of this matrix
        :return: a MathMatrix that is the transpose of this MathMatrix
        """
        transpose = []
        transpose_rows = self.get_num_cols()
        transpose_cols = self.get_num_rows()

        for i in range(transpose_rows):
            transpose.append([])
            for j in range(transpose_cols):
                transpose[i].append(self.get_val(j, i))

        return MathMatrix(transpose)

    def is_upper_triangular(self) -> bool:
        """
        Determine if this matrix is upper triangular
        :return: True if this matrix is upper triangular, False otherwise
        """
        if self.get_num_rows() != self.get_num_cols():
            return False

        for i in range(1, self.get_num_rows()):
            for j in range(i):
                if self.get_val(i, j) != 0:
                    return False

        return True

    def __eq__(self, other):
        if not isinstance(other, MathMatrix):
            return False

        # other is a MathMatrix check to see if the sizes are the same
        if other.get_num_rows() != self.get_num_rows() or other.get_num_cols() != \
                self.get_num_cols():
            return False

        for i in range(self.get_num_rows()):
            for j in range(self.get_num_cols()):
                if self.get_val(i, j) != other.get_val(i, j):
                    return False

        return True

    @staticmethod
    def __rectangular_matrix(mat: List[List[int]]) -> bool:
        """
        Helper method used in the precondition check for the constructor
        :param mat: check if this matrix is rectangular
        :return: false if this matrix is not rectangular, true otherwise
        """
        if mat is None or len(mat) == 0:
            raise TypeError('Violation of preconditions: mat cannot be None or have length of 0')

        is_rectangular = True
        row = 1
        __columns = len(mat[0])
        while is_rectangular and row < len(mat):
            is_rectangular = len(mat[row]) == __columns
            row += 1

        return is_rectangular
