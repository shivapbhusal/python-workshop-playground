#This program calculates whether the list is sorted or not 
def is_sorted(myList):
    for i in range(len(myList)-1):
        if myList[i]>myList[i+1]:
            return 'NO'
    return 'YES'

myList1=[1,2,5,4,3]
myList2=[2,3,4,5]
myList3=[1,2,3,4,5,3]
print(is_sorted(myList1))
print(is_sorted(myList2))
print(is_sorted(myList3))


