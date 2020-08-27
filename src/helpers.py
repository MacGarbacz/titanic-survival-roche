#Function to assign age of a passenger to 1 of 10 available categories
def catregorize_age(age):
    if age < 10:
        return 0
    if age < 18:
        return 1
    if age < 22:
        return 2
    if age < 25:
        return 3
    if age < 28:
        return 4
    if age < 30:
        return 5
    if age < 35:
        return 6
    if age < 42:
        return 7
    if age < 55:
        return 8
    if age < 85:
        return 9