def left_join(st):
    return ','.join(i.replace('right', 'left') for i in st)

print(left_join(("left", "right", "left", "stop")))

def three_words(st):
    count = 0
    for i in st:
        if i.isalpha():
            count += 1
        if count == 3:
            return True
        elif i.isalpha():
            count = 0
    return False

print(three_words("He is 123 man"))


def first_word(st):
    return st.replace(' ', '').replace('.', ' ')[0]

print(first_word(" a word "))


from datetime import date, timedelta
def days_diff(a, b):
    f = date(*a)
    l = date(*b)
    return abs(f-l).days

print(days_diff((1982, 4, 19), (1982, 4, 22)))
    
    
