print("""
 CCC             l                       l              t                  
C                l                       l              t                  
C         aa     l      ccc     u  u     l      aa     ttt     ooo     rrr 
C        a a     l     c        u  u     l     a a      t      o o     r   
 CCC     aaa     l      ccc      uuu     l     aaa      tt     ooo     r   
""")


def add(x, y):
    """This function returns the sum of two integers"""
    return x + y
def subtract(x, y):
    """This function returns the difference between two integers"""
    return x - y
def multiply(x, y):
    """This function returns the product of two integers"""
    return x * y
def divide(x, y):
    """This function returns the quotient of two integers"""
    return x/y

do_again = True

while (do_again):
    print("\nHello there! Welcome to the great kirikaalan show\n")
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    operation = input("'+' for addition\n'-' for subtraction\n'*' for multiplication\n'/' for divison\nEnter the operation that you want to execute: ")
    if operation == '+':
        output = add(a,b)
        print(f"{a}{operation}{b} = {output}")
    elif operation == '-':
        output = subtract(a,b)
        print(f"{a}{operation}{b} = {output}")
    elif operation == '*':
        output = multiply(a,b)
        print(f"{a}{operation}{b} = {output}")
    elif operation == '/':
        output = divide(a,b)
        print(f"{a}{operation}{b} = {output}")
    else:
        print("Wrong choice!! Please choose a proper operation")
    
    want_to_continue = input("Want to do more calculations ?\ntype 'Yes' to continue and type 'No' to terminate: ")
    if want_to_continue.lower() == "no":
        do_again = False
        print("Thank You!")