#Function to get the number
def get_number():
    try:
        number = int(input("\nEnter a number or type '0' to exit: "))
        if number == 0:
            exit()
        check_number(number)
    except ValueError:
        print("Enter a valid integer. ")
        get_number()

#Funciton to confirm the input is no zero and positive
def check_number(number):
    if number <= 0:
        print("Enter a valid positive integer.")
        get_number()
    else:
        factorial(number)

#Main algorithm
def factorial(number):
    results = 1
    number_copy = number
    while number > 1:
        results = number * results
        number -= 1
    print(f"{number_copy}! = {results}")

if __name__ == "__main__":
    get_number()