# Program to demonstrate the use of lists 

myList=[1,2,3,4,5] # creating a list 
print(myList)   # printing the list

myList.append(6) # Appending 6 to the list 
print("List after appending 6: "+str(myList))  

length=len(myList) # Length or the number of elements in the list
print(length) 

del myList[0] # Deletes the 0th element from the list. 
print("List after deleting element on 0th index" +str(myList))

print("Printing all elemnts of list using for loop")
for elements in myList:   # Printing all the elements of list using for loop
    print(elements)

