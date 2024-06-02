def main():
    password = get_password()
    stars(password)

def get_password():
    MIN_LENGTH = 6
    password = input("Enter the password: ")
    while (len(password) < MIN_LENGTH):
        print("Invaild length")
        password = input("Enter the password: ")
    return password

def stars(password):
    length = len(password)
    print('*' * length)

main()