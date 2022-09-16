"""This is my Bank System Task"""
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
        if not doesFileExists('Banks'):
            create_folder('Banks')

        bank_in = f'Banks/{self.bank_name}.json'
        if os.path.isfile(bank_in):
            print("\n****************************")
            print("Bank is already exist !")
            print("****************************")
            return True
        else:
            if not doesFileExists('Users'):
                create_folder('Users')
                create_folder(f'Users/{self.bank_name}')
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
            print("\n****************************")
            print("User is already exist !")
            print("****************************")
            return True


class Transactions:
    """This class created for make transactions"""

    def __init__(self, amount, t_type, before_bal):
        self.amount = amount
        self.t_type = t_type
        self.before_bal = before_bal


if __name__ == "__main__":
    while True:
        print("\n1) Create Account \n2) Login \n3) Delete Bank \n4) Create Bank")
        choice = int(input("Enter : "))

        if choice == 1:
            uname = input("\nEnter user name : ")
            u_pin = int(input("Enter PIN : "))
            bank_name = input("Enter Bank name : ")

            u = User(uname, u_pin, bank_name)
            if not u.check_user():
                user_in = f'Users/{bank_name}/{uname}.json'
                create_json(user_in, u)

        elif choice == 2:
            uname = input("\nEnter user name : ")
            u_pin = int(input("Enter PIN : "))
            bank_name = input("Enter Bank name : ")
            user_in = f'Users/{bank_name}/{uname}.json'
            with open(user_in, 'r+') as file:
                data = json.load(file)
            if data['username'] == uname and data['pin'] == u_pin:
                while True:
                    print("\n1) Deposit\n2) Withdraw \n3) Show transaction history "
                          "\n4) Check balance \n5) Delete Account \n6) Change your PIN \n7) Logout")
                    user_choice = int(input('Enter choice : '))

                    if user_choice == 1:
                        T_TYPE = "DEPOSIT"
                        before_balance = data['init_amount']
                        dp_amount = int(input('\nEnter amount : '))
                        t = Transactions(dp_amount, T_TYPE, before_balance)
                        data['init_amount'] += dp_amount
                        data['tr_history'].insert(0, t.__dict__)
                        if len(data['tr_history']) >5:
                            data['tr_history'].pop()
                        with open(user_in, 'r+') as file:
                            json.dump(data, file)
                        print(data)


                    elif user_choice == 2:
                        T_TYPE = "Withdraw"
                        before_balance = data['init_amount']
                        wd_amount = int(input('\nEnter amount : '))
                        t = Transactions(wd_amount, T_TYPE, before_balance)
                        data['init_amount'] -= wd_amount
                        data['tr_history'].insert(0, t.__dict__)
                        if len(data['tr_history']) > 5:
                            data['tr_history'].pop()
                        with open(user_in, 'r+') as file:
                            json.dump(data, file)
                        print(data)

                    elif user_choice == 3:
                        print(data['tr_history'])

                    elif user_choice == 4:
                        print(data['init_amount'])

                    elif user_choice == 5:
                        if os.path.isfile(user_in):
                            os.remove(user_in)

                        print("\n****************************")
                        print("Delete Account successful !")
                        print("****************************")
                        break

                    elif user_choice == 6:
                        u_pin = int(input("Enter PIN : "))
                        if u_pin == data['pin']:
                            new_pin = int(input("Enter new PIN : "))
                            reenter_pin = int(input("Re-Enter new PIN : "))
                            if new_pin == reenter_pin:
                                data['pin'] = reenter_pin
                                with open(user_in, 'r+') as file:
                                    json.dump(data, file)
                                print(data)
                            else:
                                print("Password don't match !")

                    elif user_choice == 7:
                        print("\n****************************")
                        print('Thank you !')
                        print("****************************")
                        break

                    else:
                        print("\n****************************")
                        print("Enter a valid Choice !")
                        print("****************************")

        elif choice == 4:
            b_name = input("\nEnter bank name : ")
            bank_obj = Bank(b_name)
            if not bank_obj.check_bank():
                bank_in = f'Banks/{b_name}.json'
                create_json(bank_in, bank_obj)
