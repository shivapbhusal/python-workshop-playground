# Hello World program in Python
    
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    result=S.replace("-","") 
    list_char=list(result)
    
    length=len(list_char)    
    index=int(length%K)
    result=""

    for i in range(0,index):
        result=result+str(list_char[i])
        if i==index-1:
            result=result+"-"
    
    while (index<length):
        for j in range(0,K):
            result=result+str(list_char[index+j])
        index=index+K
        if index!=length:
            result=result+"-"
    
    result=result.upper()
    return result 

result_string=solution("abc-def",2)
print(result_string)
