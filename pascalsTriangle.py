def pascalsTriangle(n):
    result = []
    for row in range(n):
        newRow = [1] * (row+1)
        result.append(newRow)
        for col in range(1,len(newRow)-1):
            newRow[col]=result[row-1][col-1] + result[row - 1][col]
    return result
                   

print(pascalsTriangle(5))

