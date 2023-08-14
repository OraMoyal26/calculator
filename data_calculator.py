import numpy as np
import pandas as pd

def resize_matrix(matrix1,matrix2,defult_num):
    max_rows = max(matrix1.shape[0], matrix2.shape[0])
    max_cols = max(matrix1.shape[1], matrix2.shape[1])

    matrix1_resized = np.pad(matrix1, ((0, max_rows - matrix1.shape[0]),
                                       (0, max_cols - matrix1.shape[1])),
                             mode='constant',constant_values=defult_num)
    matrix2_resized = np.pad(matrix2, ((0, max_rows - matrix2.shape[0]),
                                       (0, max_cols - matrix2.shape[1])),
                             mode='constant',constant_values=defult_num)

    return matrix1_resized,matrix2_resized


def plus(matrix1,matrix2):
    if matrix1.shape!=matrix2.shape:
        matrix1,matrix2=resize_matrix(matrix1,matrix2,defult_num=0)
    return matrix1+matrix2

def minus(matrix1,matrix2):
    if matrix1.shape!=matrix2.shape:
        matrix1,matrix2=resize_matrix(matrix1,matrix2,defult_num=0)
    return matrix1-matrix2

def multiply(matrix1,matrix2):
    if matrix1.shape!=matrix2.shape:
        matrix1,matrix2=resize_matrix(matrix1,matrix2,defult_num=1)
    return matrix1*matrix2

def divide(matrix1,matrix2):
    if matrix1.shape!=matrix2.shape:
        matrix1,matrix2=resize_matrix(matrix1,matrix2,defult_num=1)
    return matrix1/matrix2