def spiralOrder(matrix):
    res = []
    while matrix:
        if matrix[0]:
            res.extend(matrix[0])  #first row
            matrix = matrix[1:]
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop()) #right side
        if matrix:
            res.extend(matrix.pop()[::-1])
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res

print(spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

#output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
                
