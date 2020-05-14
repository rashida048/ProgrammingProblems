def sort_by_ext(files):
    return sorted(files, key=lambda x: x.split('.')[-1] if x[0] != '.' else x.split('.')[0])


print(sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']))
print(sort_by_ext(['1.cad', '1.', '1.aa']))
    
def sort_by_ext1(files):
    one = []
    two = []
    for i in files:
        if i[0] == '.':
            one.append(i)
        else:
            two.append(i)
    return one + sorted(two, key=lambda x: x.split('.')[-1])
