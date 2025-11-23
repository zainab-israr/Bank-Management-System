from bank.account import Account
from bank.db import Database

def main():
    db = Database('database.db')
    db.create_table()
    
    while True:
        print("\n--- Bank Management System ---")
        print("1. Add Account")
        print("2. View Account")
        print("3. View All Accounts")
        print("4. Update Account")
        print("5. Delete Account")
        print("6. Deposit")
        print("7. Withdraw")
        print("0. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            Account.add_account(db)
        elif choice == '2':
            Account.view_account(db)
        elif choice == '3':
            Account.view_all_accounts(db)
        elif choice == '4':
            Account.update_account(db)
        elif choice == '5':
            Account.delete_account(db)
        elif choice == '6':
            Account.deposit(db)
        elif choice == '7':
            Account.withdraw(db)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
