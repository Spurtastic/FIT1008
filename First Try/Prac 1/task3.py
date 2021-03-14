def print_menu():
    """
    :return: no return
    :raises: no exceptions
    :complexity: best case O(1) worst case O(1)"""
    print('\nMenu:')
    print('1. Decimal to HexaDecimal')
    print('2. Decimal to Binary')
    print('3. quit')


def dec_to_bin(number):
    """

    :param number: a decimal value ot be converted into decimal
    :return: returns a string containing the binary translation of the decimal number
    :raises: no exceptions
    :complexity: Best case O(n) Wo
    
    rst Case O(n)
    """
    bin = ""
    while number != 0:
        bin += str(number % 2)
        number = number // 2
    return bin


def dec_to_hexa(number):
    """

    :param number: a decimal value to be converted to a hexadecimal value
    :return: returns a string containing the hexadecimal translation of the decimal number
    :raises: no exceptions
    :complexity: Best Case O(n) Worst Case O(n)
    """
    hex = ""
    while number != 0:
        remainder = number % 16
        if remainder < 10:
            hex += str(remainder)
        elif remainder == 10:
            hex += "A"
        elif remainder == 11:
            hex += "B"
        elif remainder == 12:
            hex += "C"
        elif remainder == 14:
            hex += "D"
        elif remainder == 15:
            hex += "E"

        number = number // 16
    return hex


def reverse_string(string):
    """

    :param string: A string to be reversed
    :return: returns a string that is a flipped version of the original text
    :raises: no exceptions
    :complexity: Best Case O(n) Worst Case O(n)
    """

    reverse = ""
    count = -1
    length = -len(string)
    while count >= length:
        reverse += string[count]
        count -= 1
    return reverse


quit = False
while not quit:
    print_menu()
    command = int(input("\nEnter command: "))

    if command == 1:
        number = int(input("Enter number in Decimal"))
        string = dec_to_hexa(number)
        print(reverse_string(string))

    elif command == 2:
        number = int(input("Enter number in Decimal"))
        string = dec_to_bin(number)
        print(reverse_string(string))

    elif command == 3:
        quit = True
