def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "ERROR: NUMBER NOT DIVISIBLE."
    else:
        return a/b
def exit_calculator():
    print("EXITING...GOOD BYE!")
def calculator():
    print(" WELCOME!WHAT DO YOU WANT ME TO DO?:+,-,*,/,exit")
    while True:
         operation=input("Enter your operation:")
         if operation=="exit":
            exit_calculator()
            break
         num1=float(input("ENTER YOUR FIRST NUMBER:"))
         num2=float(input("ENTER YOUR SECOND NUMBER:"))
         if operation=="-":
             print("AFTER SUBTRACTING:",sub(num1,num2))
         elif operation=="*":
             print("AFTER MULTIPLYING:",multiply(num1,num2))
         elif operation=="/":
             print("AFTER DIVIDING:",divide(num1,num2))
         elif operation=="+":
             print("AFTER ADDING:",add(num1,num2))
             
         else:
             print("OOPS!INVALID OPERATION.PLEASE TRY AGAIN...")
calculator()
