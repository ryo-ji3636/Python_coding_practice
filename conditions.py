#practice of making if sentences
n = int(input("Enter the integer -> "))

if (n > 0):
    print("Positive")
elif (n < 0):
    print("Negative")
else:
    print("Zero")


#dividing score into each grade
def get_grade(score):
    if (score >= 90):
        return "A"
    elif (score >= 80):
        return "B"
    elif (score >= 70):
        return "C"
    elif (score >= 60):
        return "D"
    else:
        return "F"

          