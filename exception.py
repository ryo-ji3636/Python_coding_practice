#making code using try and except
try:
    n = str(input("What's integer? -> "))
    print(int(n))

except ValueError:
    print("Invalid integer entered.")

#make user enter two number and then process error and non-error
try: 
    x = float(input("What's x? -> "))
    y = float(input("What's y? -> "))
    z = x / y
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(z)
finally:
    print("Excuting successfully.")
    