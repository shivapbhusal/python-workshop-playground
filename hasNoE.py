#This program checks if a word has E and Z in it . 
def hasNoE(word):
    result='True'
    for letters in word:
        if letters=='E'or letters=='e':
            return 'False'
        else:
            result='True'
    return result

def hasNoZ(word):
    result='True'
    for letters in word:
        if letters=='Z' or letter=='z':
	    return 'False'
	else:
	     result='True'
    return result

             
count_total=0 
count_noE=0
count_noZ=0
fin=open('words.txt')
for line in fin:
    count_total=count_total+1
    word=line.strip()
    if hasNoE(word)=='True':
        count_noE=count_noE+1 
        print(word)
    if hasNoZ(word)=='True':
        count_noZ=count_noZ+1
percentageE =(float(count_noE)/float(count_total))*100
percentageZ=(float)(count_noZ)/float(count_total))*100
print('Total percentage of words not having E:')
print(percentageE)
print('Total percentage of words not having Z:')
print(percentageZ)

