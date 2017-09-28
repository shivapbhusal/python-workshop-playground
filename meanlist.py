# a program to calculate mean
def calculateMean( myList):
    sum=0
    count=0
    for numbers in myList:
        numbers=int(numbers)
        sum=sum+numbers 
        count=count+1 
    mean=float(sum)/float(count)
    return mean 

L1=[1,2,3]
L2=[4,4,7,10]
L3=[1,2,3,1,2,3]
L4=[L1,L2,L3]

for myList in L4:
    mymean=calculateMean(myList)
    print(mymean)

        
        
