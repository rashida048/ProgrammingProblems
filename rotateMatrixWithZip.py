def rotate_matrix(a):
    rotated = []
    for col in zip(*a):
        rotated.append(list(reversed(col)))
    return rotated
        
print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))


        
