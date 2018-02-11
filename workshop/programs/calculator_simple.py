# A simple calculator for addition, substraction, multiplication and division operations. 

def addition(num1, num2):  # This is defining a function. 
    sum=int(num1)+int(num2) 
    return sum 

def substraction(num1, num2):
    diff=int(num1)-int(num2) 
    return diff 

def division(num1, num2):
    div=int(num1)/int(num2) 
    return div 

def mult(num1, num2):
    product=int(num1)*int(num2) 
    return product 

a=input("Enter the first number: ")
b=input("Enter the second number: ")
operator=input("Enter d for division, a for addition, s for substraction, m for multiplication: ")
result=0
if operator=='d':
	result=division(a,b)
elif operator=='a':
	result=addition(a,b)
elif operator=='s':
	result=substraction(a,b)
elif operator=='m':
	result=mult(a,b)
else:
	print("You entered wrong operator")

print("Result: "+str(result))
	






