def find_quotes(a):
    res = []
    i = 0
    while i < len(a):
        if a[i] == '"':
            n = a[i+1:].find('"') +i+1
            word = a[i+1:n]
            res.append(word)
            i = n+1
        else:
            i+=1
    return res
    
print(find_quotes('"Greetings"'))

print(find_quotes('"this" doesn\'t make any "sense"'))

