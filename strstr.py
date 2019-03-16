#Return the index of the first occurrence of needle in haystack,
#or -1 if needle is not part of haystack.

def str(h, n):
    if n == "":
        return 0
    l = len(n)
    i = 0
    ind = 0
    while i < len(h):        
        s = i+l        
        if h[i:s] == n:                        
            return i
        i += 1
    return -1
    
    
print(str('hello', 'll'))
print(str('aaaaa', 'bba'))
print(str('', 'a'))

