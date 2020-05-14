def words_order(text, words):
    try:
        idx = [text.split().index(w) for w in words]
        return all(i < j for i, j in zip(idx, idx[1:]))
    except ValueError:
        return False
    
print(words_order('hi world im here', ['country', 'world']))
    
        
        
def words_order1(text, words):
    if len(words) ==1 and words[0] not in text:
        return False
    for i in range(0, len(words)-1):
        if words[i] not in text:
            return False
        if text.find(words[i]) >= text.find(words[i+1]):
            return False
    return True
    
