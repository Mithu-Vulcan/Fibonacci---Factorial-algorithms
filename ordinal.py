def ordinal(number):
    digits = [int(d) for d in str(number)]
    length = len(digits)
    exception_set = {1, 2, 3}

    if str(number) == "1":
        ordinal_number = str(number) + "st"
        return ordinal_number

    if digits[length - 1] in exception_set and digits[length - 2] != 1:
        match digits[length - 1]:
            case 1:
                ordinal_number = str(number) + "st"
                return ordinal_number
            case 2:
                ordinal_number = str(number) + "nd"
                return ordinal_number
            case 3:
                ordinal_number = str(number) + "rd"
                return ordinal_number

    else:
        ordinal_number = str(number) + "th"
        return ordinal_number
    
def main():
    ordinal(int(input("Enter a number: ")))

if __name__ == "__main__":
    main()