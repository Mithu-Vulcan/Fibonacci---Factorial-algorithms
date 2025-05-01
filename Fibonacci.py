from ordinal import ordinal

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
        sequence(number)

#Main Algorithm
def sequence(number):
    a = 0
    b = 1
    count = 2
    match number:
        case 1:
            print(f"{ordinal(1)} number: {a}")
            get_number()
        case 2:
            print(f"{ordinal(1)} number: {a}\n{ordinal(2)} number: {b}")
            get_number()
        case _:
            print(f"{ordinal(1)} number: {a}\n{ordinal(2)} number: {b}")
            while True:
                if count < number:
                    f = a + b
                    count += 1
                    print(f"{ordinal(count)} number: {f}")
                    a, b = b, f
                else:
                    get_number()


if __name__ == "__main__":
    get_number()