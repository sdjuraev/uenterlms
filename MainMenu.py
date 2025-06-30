
class Menu:
    def menu_show(self):
        userType = int(input("Select user type"))
        if userType == 1:
            print("Librarian")
            username = input("Login: ")
            password = input("Password: ")
            return userType, username, password

        if userType == 2:
            print("User")
            username = input("Username: ")
            password = input("Password: ")
            return userType, username, password
