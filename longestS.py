def longestS(st):
    list = []
    sub = ""
    for s in st:
        if s not in sub:
            sub += s
        else:
            list.append(sub)
            sub = s
    return max(list, key=len)


print(longestS("bbbbb"))
print(longestS("pwwkew"))
print(longestS("abcabcbb"))
