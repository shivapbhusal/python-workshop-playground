#This program checks if a word has E in it . 
def hasNoE(word):
    result='True'
    for letters in word:
        if letters=='E'or letters=='e':
            return 'False'
        else:
            result='True'
    return result 
             
count_total=0 
count_noE=0
fin=open('words.txt')
for line in fin:
    count_total=count_total+1
    word=line.strip()
    if hasNoE(word)=='True':
        count_noE=count_noE+1 
        print(word)
percentage =(float(count_noE)/float(count_total))*100
print('Total percentage of words not having E:')
print(percentage)

