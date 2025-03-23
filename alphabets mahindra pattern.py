a=int(input("Enter a number"))
b=-1
for i in range(a):
    b=b+2
alphabets=""
alphabets_rev=""
space=" "
for i in range(65,65+a):
    alphabets=alphabets+chr(i)
    alphabets_rev=chr(i)+alphabets_rev
    print(alphabets+space*b+alphabets_rev)
    b=b-2
i=i+1
alphabets=alphabets+chr(i)
alphabets_rev=chr(i)+alphabets_rev
print(alphabets+space*b+alphabets_rev[1:])
for i in range(len(alphabets)):
    alphabets=alphabets[:-1]
    alphabets_rev=alphabets_rev[1:]
    b=b+2
    print(alphabets+space*b+alphabets_rev)
