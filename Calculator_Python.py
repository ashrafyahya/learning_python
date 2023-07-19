print("This is a calculator written with Python!\n")

#just learning python basics
#calculator with if
start=1
while start:
  
  option=input("Please choose an operation *+-/:\t")
  first_number=int(input("Enter first number: "))
  second_number=int(input("Enter second number: "))
  
  operations_dict= {"*": "multiplication", "+":"addition", "-":   
  "substraction", "/":"division"}
  operation= operations_dict.get(option,-1)
  #print(operation)
  
  if option == "*":
    result= first_number * second_number
  
  elif option == "+":
    result= first_number+second_number
  
  elif option == "-":
    result= first_number - second_number
  
  elif option == "/":
    result= first_number/second_number
  
  else:
    print("Try again!")
  
  print(f"The {operation}'s result is: {result}\n")
  start= int(input("Press 0 for end or 1 to continue:\t"))