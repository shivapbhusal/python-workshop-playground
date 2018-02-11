# Reads and prints words from words.txt having more than 20 characters 
myFile=open('words.txt')
for line in myFile:
    word=line.strip()
    if len(word)>20:
        print(word)
