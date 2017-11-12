# Python program to test if two strings are reverse of each other 

def is_reverse(str1, str2):
    if len(str1)!=len(str2):
        return 'NO'
    else:
        for i in range(0,len(str1)):
            if str1[i]!=str2[len(str1)-i-1]:
                return 'NO'
        return 'YES'

decision=is_reverse("hello","olleh")

decision2=is_reverse("hello","hellow")

print(decision)
print(decision2)
    
