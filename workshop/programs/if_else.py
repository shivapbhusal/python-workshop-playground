# Demo of if else statements 
# Symbol "#" is used to make comments in the program.


a=input("enter the first number: ")  # Gets input from the user 
b=input("Enter the second program: ")
sum=int(a)+int(b)                   # int(a) makes sure that a is a number 


print(sum);
if (sum>10):                        # if (condition_1)
    print("sum is greater than 10");

elif(sum==10):
    print("sum is equal to 10");

else:
    print("sum is less than 10");
