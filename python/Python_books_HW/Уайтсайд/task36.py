def matrix_multiply(left_matrix: list[list[int]], right_matrix: list[list[int]]) -> list[list[int]]:
    '''Multiplies two matrixes'''
    rows_left = len(left_matrix)
    cols_left = len(left_matrix[0])
    cols_right = len(right_matrix[0])
    result = [[0] * cols_right for _ in range(rows_left)]
    for i in range(rows_left):                     
        for j in range(cols_right):                
            total = 0
            for k in range(cols_left):              
                total += left_matrix[i][k] * right_matrix[k][j]
            result[i][j] = total
    return result   

A = [[2, 3], [4, 5]]
B = [[10, 15], [5, 1]]
print(matrix_multiply(A, B))