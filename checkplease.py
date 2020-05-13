import math

def split_check(total, number_of_people):
    if number_of_people <=1:
        raise ValueError("You can't split the check with yourself")
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("How bad is it? Gimme the total  "))
    number_of_people = int(input("How big is your crew?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
     print("Oh no! That's not a valid value, try again..")
     print("( {} )".format(err))
else:
    print("Each person owes ${}".format(amount_due))
