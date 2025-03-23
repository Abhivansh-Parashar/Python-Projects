space=" "
star="*"
a=int(input("Enter a no."))
b=-1
print(star*(a*2+1))
i=a+1
while(i>=3):
    i=i-1
    b=b+2
    print(star*i+b*space+star*i)
b=b+2
i=0
while(i<a):
    i=i+1
    print(star*i+b*space+star*i)
    b=b-2
print(star*(a*2+1))
