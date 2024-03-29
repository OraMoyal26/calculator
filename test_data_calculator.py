from data_calculator import *
import pandas as pd
import pytest


def test_plus_frame():
    frame1=pd.DataFrame([[5,6],[7,8]])
    frame2=pd.DataFrame([[1,2],[3,4]])
    expected_frame=pd.DataFrame([[6,8],[10,12]])
    pd.testing.assert_frame_equal(plus(frame1,frame2),expected_frame)

def test_minus_frame():
    frame1=pd.DataFrame([[5,6],[7,8]])
    frame2=pd.DataFrame([[1,2],[3,4]])
    expected_frame=pd.DataFrame([[4,4],[4,4]])
    pd.testing.assert_frame_equal(minus(frame1,frame2),expected_frame)

def test_multiply_frame():
    frame1=pd.DataFrame([[5,6],[7,8]])
    frame2=pd.DataFrame([[1,2],[3,4]])
    expected_frame=pd.DataFrame([[5,12],[21,32]])
    pd.testing.assert_frame_equal(multiply(frame1,frame2),expected_frame)

def test_divide_frame():
    frame1=pd.DataFrame([[5,6],[9,8]])
    frame2=pd.DataFrame([[1,2],[3,4]])
    expected_frame=pd.DataFrame([[5,3],[3,2]])
    expected_frame=expected_frame.astype(float)
    pd.testing.assert_frame_equal(divide(frame1,frame2),expected_frame)


def test_plus_matrix():
    matrix1 = np.array([[5,6],[7,8]])
    matrix2 = np.array([[1,2],[3,4]])
    expected_matrix=np.array([[6,8],[10,12]])
    np.testing.assert_array_equal(plus(matrix1,matrix2),expected_matrix)

def test_minus_matrix():
    matrix1 = np.array([[5,6],[7,8]])
    matrix2 = np.array([[1,2],[3,4]])
    expected_matrix=np.array([[4,4],[4,4]])
    np.testing.assert_array_equal(minus(matrix1,matrix2),expected_matrix)

def test_multiply_matrix():
    matrix1 = np.array([[5,6],[7,8]])
    matrix2 = np.array([[1,2],[3,4]])
    expected_matrix=np.array([[5,12],[21,32]])
    np.testing.assert_array_equal(multiply(matrix1,matrix2),expected_matrix)

def test_divide_matrix():
    matrix1 = np.array([[5,6],[9,8]])
    matrix2 = np.array([[1,2],[3,4]])
    expected_matrix=np.array([[5,3],[3,2]])
    expected_matrix=expected_matrix.astype(float)
    np.testing.assert_array_equal(divide(matrix1,matrix2),expected_matrix)


def test_plus_matrix_unequal_size():
    matrix1 = np.array([[5,6,1],[7,8,1]])
    matrix2 = np.array([[1,2],[3,4]])
    expected_matrix=np.array([[6,8,1],[10,12,1]])
    np.testing.assert_array_equal(plus(matrix1,matrix2),expected_matrix)

def test_minus_matrix_unequal_size():
    matrix1 = np.array([[5,6,1],[7,8,1]])
    matrix2 = np.array([[1,2],[3,4]])
    expected_matrix=np.array([[4,4,1],[4,4,1]])
    np.testing.assert_array_equal(minus(matrix1,matrix2),expected_matrix)

def test_multiply_matrix_unequal_size():
    matrix1 = np.array([[5,6],[7,8]])
    matrix2 = np.array([[1,2],[3,4],[2,5]])
    expected_matrix=np.array([[5,12],[21,32],[2,5]])
    np.testing.assert_array_equal(multiply(matrix1,matrix2),expected_matrix)

def test_divide_matrix_unequal_size():
    matrix1 = np.array([[5,6,1],[9,8,2],[4,5,3]])
    matrix2 = np.array([[1,2],[3,4]])
    expected_matrix=np.array([[5,3,1],[3,2,2],[4,5,3]])
    expected_matrix=expected_matrix.astype(float)
    np.testing.assert_array_equal(divide(matrix1,matrix2),expected_matrix)


def test_matrix_multiply():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_matrix=np.array([[19,22],[43,50]])
    np.testing.assert_array_equal(matrix_multiply(matrix1,matrix2),expected_matrix)

def test_matrix_multiply_dimensions_are_not_match():
    matrix1 = np.array([[5, 6, 1], [9, 8, 2], [4, 5, 3]])
    matrix2 = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError, match="The dimensions of the matrices are not match"):
        matrix_multiply(matrix1,matrix2)

