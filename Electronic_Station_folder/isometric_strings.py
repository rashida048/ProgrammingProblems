def isometric_strings(s1, s2):
    dict = {}
    for i in range(len(s1)):
        if s1[i] in dict and dict[s1[i]] != s2[i]:
            return False
        dict[s1[i]] = s2[i]
    return True

print(isometric_strings('add', 'egg'))
print(isometric_strings('foo', 'bar'))
            
    
