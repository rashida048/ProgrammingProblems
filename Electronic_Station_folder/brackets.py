def brackets(text):
    res = ''
    dict = {'(': ')', '{': '}', '[': ']'}
    for i in range(len(text)):
        if text[i] in '[{(':
            res += text[i]
        elif text[i] in ')}]':
            if len(res) == 0:
                return False
            else:
                p = res[-1]
                res = res[:len(res)-1]
                if dict[p] != text[i]:
                    return False
    if len(res) != 0:
        return False
    return True

print(brackets("((5+3)*2+1)"))
print(brackets("(3+{1-1)}"))


                
            
def brackets1(text):
    res = []
    dict = {'(': ')', '{': '}', '[': ']'}
    for i in text:
        if i in '({[':
            res.append(i)
        elif (i in ')}]') and (not res or (res and dict[res.pop()] != i)):
            return False
    return not res
             
print(brackets1("((5+3)*2+1)"))
print(brackets1("(3+{1-1)}"))
 
                   
