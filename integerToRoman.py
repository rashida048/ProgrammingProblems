def intToRoman(n):
    dic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC',
           50: 'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    res = ''
    for k in dic:
        while(n%k != n):
            res += dic[k]
            print(res)
            n -= k
    return res

#print(intToRoman(1994))
#print(intToRoman(3))
print(intToRoman(4))
        
    


