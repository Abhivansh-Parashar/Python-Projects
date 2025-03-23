import math as m

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return"Cannot divide by zero"
    return x/y

def sq_root(x):
    if x<0:
        return"Cannot take the square root of a negative number"
    return x**0.5

def power(x,y):
    return x**y

def factorial(x):
    if x<0:
        return"Factorial is not defined for negative numbers"
    if x==0:
        return 1
    fact=1
    for i in range(1,int(x) + 1):  
        fact*=i
    return fact

def root(x,y):
    if y==0:
        return"Not possible"
    return x**(1 / y)

def trigonometry(x,func):
    return func(x)

def logarithm(x):
    if x<=0:
        return"Logarithm is undefined for non-positive numbers"
    return m.log10(x)

def rad_to_degree_converter(x):
    return m.degrees(x)

def degr_to_rad_converter(x):
    return m.radians(x)

print("Welcome to Calc")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square root")
print("6. Power")
print("7. Factorial")
print("8. Root")
print("9. Trigonometry")
print("10. Logarithm to base 10")
print("11. Radian to degree converter")
print("12. Degree to radian converter")
print()

while True:
    try:
        choice = int(input("Enter choice (1-12): "))
        if choice in (1, 2, 3, 4, 6, 8):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice==1:
                print(num1,"+",num2,"=",add(num1,num2))
            elif choice==2:
                print(num1,"-",num2,"=",subtract(num1,num2))
            elif choice==3:
                print(num1,"*",num2,"=",multiply(num1,num2))
            elif choice==4:
                print(num1,"/",num2,"=",divide(num1,num2))
            elif choice==6:
                print(num1,"^",num2,"=",power(num1,num2))
            elif choice==8:
                print(num1,"root",num2,"=",root(num1,num2))
        elif choice==5:
            num1=float(input("Enter number: "))
            print("√",num1,"=",sq_root(num1))
        elif choice==7:
            num1=int(input("Enter number: "))
            print(num1,"! =",factorial(num1))
        elif choice==9:
            angle=float(input("Enter angle in radians: ")) 
            trig_func=input("Choose trigonometric function (sin, cos, tan): ").lower()
            if trig_func=="sin":
                print(f"sin({angle})=",trigonometry(angle, m.sin))
            elif trig_func=="cos":
                print(f"cos({angle})=",trigonometry(angle, m.cos))
            elif trig_func=="tan":
                print(f"tan({angle})=",trigonometry(angle, m.tan))
            else:
                print("Invalid trigonometric function")
        elif choice==10:
            num1=float(input("Enter number: "))
            print("log10(",num1,")=",logarithm(num1))
        elif choice==11:
            num1=float(input("Enter angle in radians: "))
            print(num1,"radian =",rad_to_degree_converter(num1),"degrees")
        elif choice==12:
            num1=float(input("Enter angle in degrees: "))
            print(num1,"degree =",degr_to_rad_converter(num1),"radians")
        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != "yes":
            print("Thank you for using Calc")
            break
    except ValueError:
        print("Invalid input, please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}") 
