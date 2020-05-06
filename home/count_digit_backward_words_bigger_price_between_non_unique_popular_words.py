def count_digits(st):
    return len([i for i in st if i.isdigit()])

print(count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year'))

def backward_string_by_word(st):
    return ' '.join(i[::-1] for i in st.split(' '))

print(backward_string_by_word('hello   world'))


def bigger_price(limit, data):
    return sorted(data, key = lambda x: x['price'], reverse=True)[:limit]

print(bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]))
    
def between_markers(st, begin, end):
    begin_index = st.find(begin)+len(begin) if begin in st else 0
    end_index = st.find(end) if end in st else len(st)
    return st[begin_index:end_index]

print(between_markers('No[/b] hi', '[b]', '[/b]'))
    
def non_unique_element(ar):
    return [i for i in ar if ar.count(i)>=2]

print(non_unique_element([1, 2, 3, 1, 3]))


def popular_words(st, ar):
    dictn = {}
    for i in ar:
        dictn[i] = st.lower().split().count(i)
    return dictn

print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))
    
    
