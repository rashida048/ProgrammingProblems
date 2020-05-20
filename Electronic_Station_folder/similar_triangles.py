       
def line(a, b):
    return ((a[0]-b[0])**2 + (a[1] - b[1])**2)**0.5

def similar_triangles1(coords_1, coords_2):
    one = []
    two = []
    for i in range(len(coords_1)):
        one.append(line(coords_1[i], coords_1[i-1]))
        two.append(line(coords_2[i], coords_2[i-1]))
    one = sorted(one)
    two = sorted(two)
    return all((one[i]/two[i]) == (one[i-1]/two[i-1]) for i in range(len(one)))

#print(similar_triangles1([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]))
print(similar_triangles1([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]))
print(similar_triangles1([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]))
        
        


