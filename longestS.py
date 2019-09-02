def lengthOfLongestSubstring(s):
    start, longest, dict = 0, 0, {}
    for ind, c in enumerate(s):
        if c in dict:
            start = max(start, dict[c] + 1)
        dict[c] = ind
        longest = max(longest, ind-start + 1)            
    return longest


