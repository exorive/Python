# Task
#
# 1. Create a loop to ask the user to enter two numbers in the terminal
# 2. Output to the terminal the result of dividing the first number by the second number
# 3. Then ask the user if he wants to continue yes/no
# 4. If the answer is no, then quit the loop
# 5. Otherwise you have to do it all over again


while True:
    try:
        first_number = float(input("Please enter first number: "))
        second_number = float(input("Please enter second number: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    res = first_number / second_number
    print(res)

    question = input("Do you want to continue? yes/no: ")
    if question == 'no':
        break



