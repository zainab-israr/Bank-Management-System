class Account:
    @staticmethod
    def add_account(db):
        name = input("Enter name: ")
        balance = float(input("Enter initial deposit: "))
        db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))
        print("Account added successfully.")

    @staticmethod
    def view_account(db):
        acc_id = int(input("Enter account ID: "))
        account = db.fetchone("SELECT * FROM accounts WHERE id=?", (acc_id,))
        if account:
            print(account)
        else:
            print("Account not found.")

    @staticmethod
    def view_all_accounts(db):
        accounts = db.fetchall("SELECT * FROM accounts")
        if accounts:
            for acc in accounts:
                print(acc)
        else:
            print("No accounts found.")

    @staticmethod
    def update_account(db):
        acc_id = int(input("Enter account ID: "))
        name = input("Enter new name: ")
        db.execute("UPDATE accounts SET name=? WHERE id=?", (name, acc_id))
        print("Account updated successfully.")

    @staticmethod
    def delete_account(db):
        acc_id = int(input("Enter account ID: "))
        db.execute("DELETE FROM accounts WHERE id=?", (acc_id,))
        print("Account deleted successfully.")

    @staticmethod
    def deposit(db):
        acc_id = int(input("Enter account ID: "))
        amount = float(input("Enter amount to deposit: "))
        db.execute("UPDATE accounts SET balance = balance + ? WHERE id=?", (amount, acc_id))
        print("Deposit successful.")

    @staticmethod
    def withdraw(db):
        acc_id = int(input("Enter account ID: "))
        amount = float(input("Enter amount to withdraw: "))
        db.execute("UPDATE accounts SET balance = balance - ? WHERE id=?", (amount, acc_id))
        print("Withdrawal successful.")
