myWords=dict()
fin=open('words.txt')
for line in fin:
    line=line.strip()
    myWords[line]=''
def is_valid_word(word):
    if word in myWords:
        return 'YES'
    else:
        return 'NO'
print(myWords)
print(is_valid_word('yes'))
print(is_valid_word('aa'))
print(is_valid_word('shivaprasadbhusal'))

