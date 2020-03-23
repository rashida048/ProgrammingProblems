'''
def increasing(n):
    tmp = 0
    for i in range(n):
        tmp += 1

def increasing(n):
    tmp = n-1
    while tmp==0:
        tmp -= 1
 '''   
def zigzagConversion(s, n):
    li = []
    for i in range(n):
        li.append('')
    li[0] += s[0]
    tmp = 0
    li[1] += s[1]
    tmp1 = 1
    for j in range(2, len(s)):
        if tmp1 == (n-1):
            li[tmp1-1] += s[j]
            tmp = tmp1
            tmp1 -= 1
            
        elif tmp1 == 0:
            li[tmp1+1] += s[j]
            tmp = tmp1
            tmp1 += 1
            
        elif tmp > tmp1:
            li[tmp1-1] += s[j]
            tmp = tmp1
            tmp1 -= 1
            
        elif tmp < tmp1:
            li[tmp1+1] += s[j]
            tmp = tmp1
            tmp1 += 1
    return (i+res for i in li)
                
        
print(zigzagConversion('PAYPALISHIRING', 3))
print(zigzagConversion('PAYPALISHIRING', 4))


def zigzagConversion1(s, n):
    li = []
    for i in range(n):
        li.append('')
    tmp = 0
    tmp1 = 1
    for j in range(len(s)):
        if tmp1 == (n-1):
            li[tmp1-1] += s[j]
            tmp = tmp1
            tmp1 -= 1
            
        elif tmp1 == 0:
            li[tmp1+1] += s[j]
            tmp = tmp1
            tmp1 += 1
            
        elif tmp > tmp1:
            li[tmp1-1] += s[j]
            tmp = tmp1
            tmp1 -= 1
            
        elif tmp < tmp1:
            li[tmp1+1] += s[j]
            tmp = tmp1
            tmp1 += 1
    return (','.join(li)).replace(',', '')
                
        
print(zigzagConversion1('PAYPALISHIRING', 3))
print(zigzagConversion1('PAYPALISHIRING', 4))  
            
            
            
        
    
