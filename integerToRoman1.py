def intToRoman(num):
    li1 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    li2 = ['M','CM','D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    res = ''
    for i in range(0, len(li1)):
        while(num%li1[i] != num):
            res += li2[i]
            num -= li1[i]
    return res

print(intToRoman(1994))
print(intToRoman(3))
print(intToRoman(4))
