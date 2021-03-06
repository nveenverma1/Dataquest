## 2. Matrix Vector Multiplication ##

import numpy as np

matrix_a = np.asarray([
    [0.7, 3, 9],
    [1.7, 2, 9],
    [0.7, 9, 2]
], dtype=np.float32)

vector_b = np.asarray([
    [1],
    [2],
    [1]
])

ab_product = np.dot(matrix_a, vector_b)
print(ab_product)

## 3. Matrix Multiplication ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

product_ab = np.dot(matrix_a, matrix_b)
product_ba = np.dot(matrix_b, matrix_a)

# print(product_ab)
# print()

## 4. Matrix Transpose ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

transpose_a = np.transpose(matrix_a)
print('transpose_a')
print(transpose_a)
print()

transpose_b = np.transpose(matrix_b)

print('transpose of transpose_a')
print(np.transpose(transpose_a))
print()

trans_ba = np.dot(transpose_b, transpose_a)
print('trans_ba')
print(trans_ba)
print()

trans_ab = np.dot(transpose_a, transpose_b)
print('trans_ab')
print(trans_ab)
print()

product_ab = np.dot(matrix_a, matrix_b)
print('transpose of product_ab')
print(np.transpose(product_ab))


## 5. Identity Matrix ##

i_2 = np.identity(2)
i_3 = np.identity(3)

matrix_33 = np.asarray([
    [0.7, 3, 1],
    [1.7, 2, 1],
    [0.7, 9, 1]
], dtype=np.float32)

matrix_23 = np.asarray([
    [1.3, 1.5, 7],
    [0.9, 2, 4]
], dtype=np.float32)

identity_23 = np.dot(i_2, matrix_23)
identity_33 = np.dot(i_3, matrix_33)


## 6. Matrix Inverse ##

matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])

def matrix_inverse_two(mat_two):
    first = mat_two[0]
    second = mat_two[1]
    
    det = first[0]*second[1] - first[1]*second[0]
    if det == 0:
        raise ValueError("The matrix isn't invertible")
    
    right_mat = np.asarray([
        [second[1], -first[1]],
        [-second[0], first[0]]
    ])
    
    inv_mat = np.dot(1/det, right_mat)
    return inv_mat

inverse_a = matrix_inverse_two(matrix_a)

i_2 = np.dot(matrix_a, inverse_a)
print(i_2)
 
    

## 7. Solving The Matrix Equation ##

matrix_a = np.asarray([
    [30, -1],
    [50, -1]
], dtype=np.float32)

vector_b = np.asarray([
    [-1000],
    [-100]
])

matrix_a_inverse = np.linalg.inv(matrix_a)
solution_x = np.dot(matrix_a_inverse, vector_b)


## 8. Determinant For Higher Dimensions ##

matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])

det_22 = np.linalg.det(matrix_22)
det_33 = np.linalg.det(matrix_33)