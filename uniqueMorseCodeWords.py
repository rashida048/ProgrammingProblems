def umcw(words):
    con = ['' for x in range(len(words))]  
    li1 = {"a":".-", "b":"-...", "c":"-.-.", "d": "-..",
           "e": ".", "f":"..-.",
           "g": "--.", "h": "....", "i": "..",
           "j": ".---", "k": "-.-", "l": ".-..",
           "m": "--", "n": "-.", "o": "---",
           "p": ".--.", "q": "--.-",
           "r": ".-.", "s": "...", "t": "-", "u": "..-",
           "v": "...-", "w": ".--",
           "x": "-..-",
           "y": "-.--", "z": "--.."}
       
    for i in range(len(words)):
        for letter in words[i]:
            con[i]+=li1[letter]
    return len(list(set(con)))
'''
    for i in con:
        if i not in unique:
            unique.append(i)
    return (len(unique))
    '''

#print(umcw(["gin", "zen", "gig", "msg"]))
#print(umcw(["gin", "zen", "gig", "msg"]))


def umcw1(words):
    con = []
    li1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
               "y", "z"]
    li2=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.",
            "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for i in range(len(words)):
        w = ''
        for letter in words[i]:
            w += (li2[li1.index(letter)])
        con.append(w)
    return len(list(set(con)))
#print(umcw(["gin", "zen", "gig", "msg"]))
    

def umcw2(words):
    con = []
    li1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
               "y", "z"]
    li2=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.",
            "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for i, w in enumerate(words):
        wd = ''
        for letter in w:
            wd += li2[ord(letter)-97]
        con.append(wd)
    return len(list(set(con)))
print(umcw2(["gin", "zen", "gig", "msg"]))
        
            
