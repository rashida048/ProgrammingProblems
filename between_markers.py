print("<head><title>My new site</title></head>".find("<title>"))


def between_markers(text, begin, end):
    begin_index = text.find(begin)+len(begin) if begin in text else 0
    end_index = text.find(end) if end in text else len(text)
    return text[begin_index:end_index]

print(between_markers('What is >apple<', '>', '<'))
print(between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>"))
print(between_markers('No[/b] hi', '[b]', '[/b]'))
print(between_markers('No [b]hi', '[b]', '[/b]'))
print(between_markers('No hi', '[b]', '[/b]'))
print(between_markers('No <hi>', '>', '<'))


        
   
