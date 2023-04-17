def letter_c(text):
    list_of_word = []
    with open(text, 'r') as my_file:
        zen_of = my_file.read()
        words = zen_of.split()
        for i in words:
            if i.startswith('C') or i.startswith('c'):
                list_of_word.append(i)
        return list_of_word
text = 'zen_of_python.txt'
list_of_word = letter_c(text)
print(list_of_word)




