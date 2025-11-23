import unittest
import os
from bank.db import Database
from bank.account import Account

class TestBankSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use a temporary database for testing
        cls.test_db_file = "test_database.db"
        cls.db = Database(cls.test_db_file)
        cls.db.create_table()

    @classmethod
    def tearDownClass(cls):
        # Remove temporary database after tests
        if os.path.exists(cls.test_db_file):
            os.remove(cls.test_db_file)

    def setUp(self):
        # Clear table before each test
        self.db.execute("DELETE FROM accounts")

    def test_add_account(self):
        # Simulate adding an account
        self.db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Alice", 1000))
        account = self.db.fetchone("SELECT * FROM accounts WHERE name=?", ("Alice",))
        self.assertIsNotNone(account)
        self.assertEqual(account[1], "Alice")
        self.assertEqual(account[2], 1000)

    def test_update_account(self):
        self.db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Bob", 500))
        account = self.db.fetchone("SELECT * FROM accounts WHERE name=?", ("Bob",))
        acc_id = account[0]

        # Update account name
        self.db.execute("UPDATE accounts SET name=? WHERE id=?", ("Bobby", acc_id))
        updated_account = self.db.fetchone("SELECT * FROM accounts WHERE id=?", (acc_id,))
        self.assertEqual(updated_account[1], "Bobby")

    def test_deposit_withdraw(self):
        self.db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Charlie", 200))
        account = self.db.fetchone("SELECT * FROM accounts WHERE name=?", ("Charlie",))
        acc_id = account[0]

        # Deposit
        self.db.execute("UPDATE accounts SET balance = balance + ? WHERE id=?", (300, acc_id))
        account_after_deposit = self.db.fetchone("SELECT * FROM accounts WHERE id=?", (acc_id,))
        self.assertEqual(account_after_deposit[2], 500)

        # Withdraw
        self.db.execute("UPDATE accounts SET balance = balance - ? WHERE id=?", (100, acc_id))
        account_after_withdraw = self.db.fetchone("SELECT * FROM accounts WHERE id=?", (acc_id,))
        self.assertEqual(account_after_withdraw[2], 400)

    def test_delete_account(self):
        self.db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("David", 700))
        account = self.db.fetchone("SELECT * FROM accounts WHERE name=?", ("David",))
        acc_id = account[0]

        # Delete account
        self.db.execute("DELETE FROM accounts WHERE id=?", (acc_id,))
        deleted_account = self.db.fetchone("SELECT * FROM accounts WHERE id=?", (acc_id,))
        self.assertIsNone(deleted_account)

if __name__ == '__main__':
    unittest.main()
