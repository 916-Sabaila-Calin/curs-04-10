def is_prime(n :int) -> bool:
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True

while True:
    print("1. Enter numbers")
    print("2. Exit")
    option = input(">")

    if option == "1":
        numbers = input("enter numbers: ")
        number_list = numbers.split()
        int_number_list = []

        for number in number_list:
            int_number_list.append(int(number))

        for number in int_number_list:
            if is_prime(number) == True:
                print(number)
    elif option == "2":
        print("bye")
        break
    else:
        print("error")