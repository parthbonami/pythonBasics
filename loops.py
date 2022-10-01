# while implementation
print("\n while loop")
i=0
while(i<10) :
    print(i)
    i +=1

print("\n\n for loop")
#for implementation
for i in range(5) :
    print(i)

print("\n\n")
n = 10
for i in range(0,n):
    print(n-i)

print("\n\n")
set = {1,2,3,4,5,6,1,2,3}
for i in set:
    print(i)


print("\n\nNested Loops")
for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print()
    
print("\n\n")
#for loop different iterator
for i in range(1,10,2):
    print(i,end=", ")

