from cryptography.fernet import Fernet

def Name(): 
    print("\nWelcome to Secure Safe")
    name = input("\nEnter your name:\n")
    print(f"\nHello {name}, how would you like to proceed?")
    return name


def generate_master_key():
    return Fernet.generate_key()


def save_master_key(master_key):
    with open("2PasswordK.key", "wb") as key_file:
        key_file.write(master_key)


def load_master_key():
    try:
        with open("2PasswordK.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("No master key found. Please enter a new master key.")
        return None


def encrypt_password(password, master_key):
    fernet = Fernet(master_key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password, master_key):
    fernet = Fernet(master_key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password


def get_master_key():
    while True:
        choice = input("\nDo you have a master key? (Yes/No): ").strip().lower()
        if choice == "yes":
            master_key = load_master_key()
            if master_key:
                return master_key
        elif choice == "no":
            master_key = generate_master_key()
            save_master_key(master_key)
            print("Your new master key has been generated and saved.")
            return master_key
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")


def Username():
    username = input("Enter your username: ").strip()
    return username


def Password():
    password = input("Enter your password: ").strip()
    return password


def Add(master_key):
    username = Username()
    password = Password()
    encrypted_password = encrypt_password(password, master_key)
    with open('2PasswordT.txt', 'a') as file:
        file.write(f"Username: {username}\n")
        file.write(f"Encrypted Password: {encrypted_password.decode()}\n")
        file.write("\n")
    print("Your username and password have been secured.")


def Remove():
    username_remove = input("Enter the username you want to remove: ").strip()
    try:
        with open('2PasswordT.txt', 'r') as file:
            lines = file.readlines()
        with open('2PasswordT.txt', 'w') as file:
            skip = False
            for i, line in enumerate(lines):
                if line.startswith(f"Username: {username_remove}"):
                    skip = True
                elif skip and line.startswith("Encrypted Password:"):
                    skip = False
                    continue
                if not skip: 
                    file.write(line)
        print(f"User '{username_remove}' has been removed.")
    except FileNotFoundError:
        print("The file '2PasswordT.txt' does not exist.")


def Read(master_key):
    try:
        with open('2PasswordT.txt', 'r') as file:
            content = file.readlines()
            if content:
                print("\nCurrent data in 2PasswordT.txt:\n")
                for i, line in enumerate(content):
                    if line.startswith("Username:"):
                        print(line.strip())
                    elif line.startswith("Encrypted Password:"):
                        encrypted_password = line.strip().split(": ")[1].encode()
                        decrypted_password = decrypt_password(encrypted_password, master_key)
                        print(f"Password: {decrypted_password}")
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print("2PasswordT.txt does not exist.")


def Clear():
    try:
        with open('2PasswordT.txt', 'w') as file:
            file.write("")
        print("All data has been cleared from 2PasswordT.txt.")
    except FileNotFoundError:
        print("2PasswordT.txt does not exist.")


def Main():
    master_key = get_master_key()
    Name()
    while True:
        print("\nPlease choose an option:")
        print("1. 'Add' Username and Password")
        print("2. 'Remove' Username and Password")
        print("3. 'Read' Stored Data")
        print("4. 'Clear' All Data")
        print("5. 'Exit'")
        choice = input("\nEnter your choice: ").strip().lower()
        if choice == "add":
            Add(master_key)
        elif choice == "remove":
            Remove()
        elif choice == "read":
            Read(master_key)
        elif choice == "clear":
            Clear()
        elif choice == "exit":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


Main()