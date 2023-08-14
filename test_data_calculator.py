from data_calculator import *
import pandas as pd

def test_plus_frame():
    frame1=pd.DataFrame([[5,6],[7,8]])
    frame2=pd.DataFrame([[1,2],[3,4]])
    expected_frame=pd.DataFrame([[6,8],[10,12]])
    pd.testing.assert_frame_equal(plus(frame1,frame2),expected_frame,check_names=False)

def test_minus_frame():
    frame1=pd.DataFrame([[5,6],[7,8]])
    frame2=pd.DataFrame([[1,2],[3,4]])
    expected_frame=pd.DataFrame([[4,4],[4,4]])
    pd.testing.assert_frame_equal(minus(frame1,frame2),expected_frame,check_names=False)

def test_multiply_frame():
    frame1=pd.DataFrame([[5,6],[7,8]])
    frame2=pd.DataFrame([[1,2],[3,4]])
    expected_frame=pd.DataFrame([[5,12],[21,32]])
    pd.testing.assert_frame_equal(multiply(frame1,frame2),expected_frame,check_names=False)

def test_divide_frame():
    frame1=pd.DataFrame([[5,6],[9,8]])
    frame2=pd.DataFrame([[1,2],[3,4]])
    expected_frame=pd.DataFrame([[5,3],[3,2]])
    expected_frame=expected_frame.astype(float)
    pd.testing.assert_frame_equal(divide(frame1,frame2),expected_frame,check_names=False)
