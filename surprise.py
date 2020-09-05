n=int(input("enter no of rows : "))
print(((input("enter FULL name of your character : ")).title()).center(50,":"))
# i
for rows in range(1,n+1):
    for cols in range(1,n+1):
        if rows==1 or rows==n or cols==(n//2+1):
            print("I", end="")
        else:
            print(end=" ")
    print()
for z in range(0,2*n):
    if z%2==0:
        print("i", end="")
    else:
        print("_", end="")
print()
# l
for rows in range(1,n+1):
    for cols in range(1,n+1):
        if rows==n or cols==1:
            print("L", end="")
        else:
            print(end=" ")
    print()
print()

# o
for rows in range(1,n+1):
    for cols in range(1,n+1):
        if rows==1 or rows==n or cols==1 or cols==n:
            print("O", end="")
        else:
            print(end=" ")
    print()
print()

# v
for rows in range(1,n+1):
    for cols in range(1,2*n):
        if cols==rows or cols == (2*n-rows):
            print("v",end="")
        else:
            print(end=" ")
    print()
print()

# e
for rows in range(1,n+1):
    for cols in range(1,n+1):
        if rows==1 or rows==n//2+1 or rows==n or cols==1 or cols ==2:
            print("E", end="")
        else:
            print(end=" ")
    print()
for z in range(0,2*n):
    if z%2==0:
        print("Love", end="")
    else:
        print("_", end="")
print()
# y
for rows in range(1,n//2+2):
    for cols in range(1,n+1):
        if cols==rows or cols==n+1-rows:
            print("y", end="")
        else:
            print(end=" ")
    print()
for i in range(n//2+2,n+1):
    for cols in range(1,n+1):
        if cols==n//2+1:
            print("y", end="")
        else:
            print(end=" ")
    print()
print()

# o
for rows in range(1,n+1):
    for cols in range(1,n+1):
        if rows==1 or rows==n or cols==1 or cols==n:
            print("O", end="")
        else:
            print(end=" ")
    print()
print()
# u
for rows in range(1,n+1):
    for cols in range(1,n+1):
        if rows==n or cols==1 or cols==n:
            print("U", end="")
        else:
            print(end=" ")
    print()
for z in range(0,2*n):
    if z%2==0:
        print("you", end="")
    else:
        print("_", end="")

print()
for z in range(0,3*n ):
    if z==8:
        print("THANK YOU SO MUCH FOR LOVING.",end="")
    print("*",end="")
input()



