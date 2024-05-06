import getpass

#add a new user to the password file
def add_user_to_file(username, real_name, password):
    with open('passwd.txt', 'a') as f:
        f.write(f"{username}:{real_name}:{password}\n")

#  check if a username already exists in the password file
def is_username_taken(username):
    with open('passwd.txt', 'r') as f:
        for line in f:
            existing_username = line.split(':')[0]
            if existing_username == username:
                return True
    return False

#  add a new user
def add_user():
    username = input("Enter new username: ")
    if is_username_taken(username):
        print("Error: Username already exists. Please choose a different username.")
        return

    real_name = input("Enter real name: ")
    password = getpass.getpa+ss("Enter password: ")
    add_user_to_file(username, real_name, password)
    print("User Created.")

#  change a user's password
def change_password():
    username = input("User: ")
    current_password = input("Current Password: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm: ")

    if new_password == confirm_password:
        # Read all lines from the file
        with open('passwd.txt', 'r') as f:
            lines = f.readlines()

        # Rewrite the file with updated password
        with open('passwd.txt', 'w') as f:
            for line in lines:
                if line.startswith(f"{username}:") and line.endswith(f":{current_password}\n"):
                    f.write(f"{username}:{line.split(':')[1]}:{new_password}\n")
                    print("Password changed.")
                    return
                else:
                    f.write(line)
        print("User not found or current password is incorrect. Nothing changed.")
    else:
        print("Passwords do not match. Nothing changed.")

# delete a user from the password file
def delete_user_from_file(username):
    with open('passwd.txt', 'r') as f:
        lines = f.readlines()

    with open('passwd.txt', 'w') as f:
        for line in lines:
            if not line.startswith(f"{username}:"):
                f.write(line)

#  delete a user
def delete_user():
    username = input("Enter username: ")
    if is_username_taken(username):
        delete_user_from_file(username)
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")

#  check if the login credentials are correct
def is_valid_login(username, password):
    with open('passwd.txt', 'r') as f:
        for line in f:
            u, _, p = line.strip().split(':')
            if u == username and p == password:
                return True
    return False

# for user login
def login():
    username = input("User: ")
    password = input("Password: ")
    if is_valid_login(username, password):
        print("Access granted.")
    else:
        print("Access denied.")

# Main function
if __name__ == "__main__":
    choice = input("Choose operation (1: Change Password, 2: Delete User, 3: Login, 4: Add User): ")

    if choice == '1':
        change_password()

    elif choice == '2':
        delete_user()

    elif choice == '3':
        login()

    elif choice == '4':
        add_user()

    else:
        print("Invalid choice.")