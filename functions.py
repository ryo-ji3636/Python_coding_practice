# I made a code that user enter the length and width
# and calculate area from them. Then printing the result

length = float(input("What's length? ->"))
width = float(input("What's width? ->"))

area = length * width

print(f"The area is {area}")


# making definition of cube calculator
def cube(n):
    result = n ** 3
    return result

