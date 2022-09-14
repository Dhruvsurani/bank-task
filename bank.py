"""This is my Bank System Task"""
import io
import json
import os


def doesFileExists(name):
    return os.path.exists(name)


def create_folder(path):
    return os.mkdir(path)


def create_json(path, obj):
    with open(os.path.join(path), 'w') as db_file:
        db_file.write(json.dumps(obj.__dict__))


class Bank:
    """This class for Creating Bank and store users details"""
    counter = 1

    def __init__(self, name):
        self.bank_name = name
        self.bank_id = Bank.counter
        Bank.counter += 1


    def check_bank(self):
        bank_in = f'Banks/{self.bank_name}.json'
        if os.path.isfile(bank_in):
            print("****************************")
            print("Bank is already exist !")
            print("****************************")

        else:
            if doesFileExists(f'Users/{self.bank_name}'):
                pass
            else:
                create_folder(f'Users/{self.bank_name}')


class User:
    """This class creates new user"""

    def __init__(self, username, pin, bank_name):
        self.username = username
        self.pin = pin
        self.bank_name = bank_name
        self.init_amount = 0
        self.tr_history = []

    def check_user(self):
        user_in = f'Users/{self.bank_name}/{self.username}.json'

        if os.path.isfile(user_in):
            print("****************************")
            print("User is already exist !")
            print("****************************")
            return True



class Transactions:
    """This class created for make transactions"""

    def __init__(self, amount, t_type, before_bal):
        self.amount = amount
        self.t_type = t_type
        self.before_bal = before_bal

    def __repr__(self):
        return self.before_bal


bank_path = "Banks"
user_path = "Users"

if __name__ == "__main__":
    while True:
        print("1) Create Account \n2) Login \n3) Delete Bank \n4) Create Bank")
        choice = int(input("Enter : "))

        if choice == 1:
            uname = input("Enter user name : ")
            u_pin = int(input("Enter PIN : "))
            bank_name = input("Enter Bank name : ")

            u = User(uname, u_pin, bank_name)
            if not u.check_user():
                user_in = f'Users/{bank_name}/{uname}.json'
                create_json(user_in, u)


        elif choice == 4:
            b_name = input("Enter bank name : ")
            bank_obj = Bank(b_name)
            bank_obj.check_bank()
            bank_in = f'Banks/{b_name}.json'
            create_json(bank_in, bank_obj)


