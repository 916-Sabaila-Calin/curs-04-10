while True:
    print("1. Enter numbers")
    print("2. Exit")
    option = input(">")

    if option == "1":
        numbers = input("enter numbers: ")
        print(numbers)
    elif option == "2":
        print("bye")
        break
    else:
        print("error")