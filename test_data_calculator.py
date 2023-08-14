from data_calculator import *
import pandas as pd


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