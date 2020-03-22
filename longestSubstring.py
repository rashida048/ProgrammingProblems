              
def longestSubstring(strs):
    small = strs[0]
    for i in range(1, len(strs)):
        if len(strs[i]) < len(small):
            small = strs[i]
    strs.remove(small)
    output = ''
    char = ''
    tmp = ''

    for i in range(len(small)):
        tmp = small[i]
        for j in range(len(strs)):
            char = strs[j][i]
            if tmp != char:
                tmp = ''
                break
        if tmp == '':
            break
        else:
            output += tmp

    return output
    
#print(longestSubstring(['flower', 'flow', 'flight']))
#print(longestSubstring(['', '']))


def longestSubstring2(strs):
    strsLength = len(strs)
    minLength = 9999
    char = ''
    output = ''
    tmp = ''

    for string in strs:
        length = len(string)
        if(minLength > length):
            minLength = length

    for i in range(minLength):
        for j in range(strsLength):
            if j == 0:
                tmp = strs[j][i]
                continue
            else:
                char = strs[j][i]
                print(char)

            if tmp != char:
                tmp = ''
                break
        if tmp == '':
            break
        else:
            output += tmp

    return output
    
print(longestSubstring2(['flower', 'flow', 'flight']))
    
