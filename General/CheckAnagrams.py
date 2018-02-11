# This program checks if two string are anagrams 
def is_anagrams(word1,word2):
    word1=list(word1)
    word2=list(word2)
    word1.sort()
    word2.sort()
    len1=len(word1)
    len2=len(word2)
    if len1==len2:
        for i in range(len1):
            if (word1[i]!=word2[i]):
                return 'NO'
        return 'YES'

    else:
        return 'NO'
print(is_anagrams('hello','olleh'))
print(is_anagrams('abc','cde'))
