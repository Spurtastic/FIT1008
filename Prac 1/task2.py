def print_menu():
    print('\nMenu:')
    print('1. append')
    print('2. reverse')
    print('3. print')
    print('4. pop')
    print('5. count')
    print('6. quit')


def reverse(my_list):
    length = len(my_list)
    for i in range(length//2):
        temp = my_list[i]
        my_list[i] = my_list[length -i-1]
        my_list[length -i-1]=temp


def pop_(list):
    length = len(list) - 1
    number = list[length]
    del list[length]
    return number 
    


def count(list, item):
    count = 0
    for n in list:
        if n == item:
            count += 1
    return count


my_list = []
quit = False
input_line = None

while not quit:
    print_menu()
    command = int(input("\nEnter command: "))

    if command == 1:
        item = input("Item? ")
        my_list.append(item)
    elif command == 2:
        reverse(my_list)
    elif command == 3:
        print(my_list)
    elif command == 4:
        print(pop_(my_list))
    elif command == 5:
        item = input("Item? ")
        print(count(my_list, item))
    elif command == 6:
        quit = True