print("-------Welcome to my simple calculator------------")
# using input from user
num1 = float(input("Enter your first value:"))
operator = input("Enter Operator(+,-,*,/ ):")
num2 = float(input("Enter your second value:"))
# Calculation
if operator == "+":
    print( "Answer is" , num1 + num2)
elif operator == "-": 
     print( "Answer is" ,  num1 - num2)
elif operator == "*": 
      print( "Answer is" ,  num1 * num2)
elif operator == "/":
       if num2 != 0:
        print( "Answer is" ,  num1 / num2)
       else :
        print("Division by zero")
else:
        print("Invalid operator")