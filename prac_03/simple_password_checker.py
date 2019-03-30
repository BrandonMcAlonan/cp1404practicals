MIN_LENGTH = 10


def get_password(min_length):
    password = input("Enter password {} characters long: ".format(min_length))
    while len(password) < min_length:
        print("Password is not long enough")
        password = input("Enter password {} characters long: ".format(min_length))
    return password


def print_asterisks(length):
    print('*' * len(length))


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


main()
