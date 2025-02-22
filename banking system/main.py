from account import BankAccount, SavingsAccount, CheckingAccount
import time
import json
import os  # To check if the data file exists

DATA_FILE = 'accounts.json'  # Name of the file to store account data

def load_accounts():
    """Load accounts from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'savings': {}, 'checking': {}}

def save_accounts(accounts):
    """Save accounts to a JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(accounts, file)

def print_menu():
    print("\n💼 Please select an option:")
    print("1. 🏦 Create a bank account")
    print("2. 💰 Withdraw from your savings account")
    print("3. 💵 Withdraw from your checking account")
    print("4. 💳 Deposit to your savings account")
    print("5. 💸 Deposit to your checking account")
    print("6. 📊 Check savings account balance")
    print("7. 🏧 Check checking account balance")
    print("8. ❌ Exit")

def create_savings_account(accounts):
    account_number = input("Enter a unique account number: ")
    if account_number in accounts['savings']:
        print("❌ An account with this number already exists!")
        time.sleep(2)
        return
    initial_balance = float(input("Enter your initial balance: "))
    account = SavingsAccount(account_number, initial_balance)
    accounts['savings'][account_number] = account.__dict__  # Store account details
    print(f"✅ Savings account created successfully with account number {account_number} and balance: {account.balance}")
    time.sleep(2)

def create_checking_account(accounts):
    account_number = input("Enter a unique account number: ")
    if account_number in accounts['checking']:
        print("❌ An account with this number already exists!")
        time.sleep(2)
        return
    initial_balance = float(input("Enter your initial balance: "))
    account = CheckingAccount(account_number, initial_balance)
    accounts['checking'][account_number] = account.__dict__  # Store account details
    print(f"✅ Checking account created successfully with account number {account_number} and balance: {account.balance}")
    time.sleep(2)

def main():
    accounts = load_accounts()  # Load accounts at the start
    while True:
        print_menu()
        choice = int(input("Enter your choice [1-8]: "))
        
        if choice == 1:
            print("Which account do you want to create? (1: Savings, 2: Checking): ")
            account_type = input("Enter your choice (1/2): ")
            if account_type == '1':
                create_savings_account(accounts)
            elif account_type == '2':
                create_checking_account(accounts)
            else:
                print("❌ Invalid account type. Please try again.")
                time.sleep(2)
        
        elif choice == 2:
            account_number = input("Enter the savings account number: ")
            if account_number in accounts['savings']:
                amount = float(input("Enter the amount to withdraw: "))
                print(accounts['savings'][account_number].withdraw(amount))
            else:
                print("❌ No savings account found with that number.")
            time.sleep(2)

        elif choice == 3:
            account_number = input("Enter the checking account number: ")
            if account_number in accounts['checking']:
                amount = float(input("Enter the amount to withdraw: "))
                print(accounts['checking'][account_number].withdraw(amount))
            else:
                print("❌ No checking account found with that number.")
            time.sleep(2)

        elif choice == 4:
            account_number = input("Enter the savings account number: ")
            if account_number in accounts['savings']:
                amount = float(input("Enter the amount to deposit: "))
                print(accounts['savings'][account_number].deposit(amount))
            else:
                print("❌ No savings account found with that number.")
            time.sleep(2)

        elif choice == 5:
            account_number = input("Enter the checking account number: ")
            if account_number in accounts['checking']:
                amount = float(input("Enter the amount to deposit: "))
                print(accounts['checking'][account_number].deposit(amount))
            else:
                print("❌ No checking account found with that number.")
            time.sleep(2)

        elif choice == 6:
            account_number = input("Enter the savings account number: ")
            if account_number in accounts['savings']:
                print(accounts['savings'][account_number].check_balance())
            else:
                print("❌ No savings account found with that number.")
            time.sleep(2)

        elif choice == 7:
            account_number = input("Enter the checking account number: ")
            if account_number in accounts['checking']:
                print(accounts['checking'][account_number].check_balance())
            else:
                print("❌ No checking account found with that number.")
            time.sleep(2)

        elif choice == 8:
            print("👋 Thank you for using the banking system. Goodbye!")
            save_accounts(accounts)  # Save accounts before exiting
            break
        else:
            print("❌ Invalid choice. Please try again.")
            time.sleep(2)

if __name__ == '__main__':
    main()
