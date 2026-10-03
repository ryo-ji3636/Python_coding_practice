#practice loops
for i in range(1,11):
    print(i)

#using while loop until entering positive number
while(True):
    n = int(input("What's positive integer? -> "))
    if n <= 0:
        continue
    else:
        print("meow" * n)
        break
