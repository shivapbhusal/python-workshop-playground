# A program to demonstrate the usage of functions. 

def addition(num1, num2): # here, addition is the function name, num1 and num2 are inputs to it, and sum is what it returns as output. 
    sum=int(num1)+int(num2)
    return sum 

a=input("Enter the first number: ")
b=input("Enter the second number: ")
mysum=addition(a,b) # Here, we call the addition function passing a and b as the parameters ( inputs ) and store the output in the variable called "mysum".
print(mysum)
