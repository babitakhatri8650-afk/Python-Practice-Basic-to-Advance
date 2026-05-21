status = int(input("Enter any number"))

match status:
    case 200:
        print("Success")

    case 404:
        print("Not found")

    case _:
        print("Unknown Status")