# Bank Management System (Python + SQLite)

## Description
This project implements a **Bank Management System** in Python using SQLite.  
It demonstrates full **CRUD operations** (Create, Read, Update, Delete) on bank accounts, along with account searches and simple transaction management.  

Developed as part of a **DBMS course project**, it showcases practical database interaction, Python programming, and object-oriented design skills.

---

## Features
- **Add Account:** Create new bank accounts with customer details and initial deposit  
- **View Account:** Check account details by account ID  
- **View All Accounts:** List all accounts in the system  
- **Update Account:** Update customer information  
- **Delete Account:** Close an account  
- **Deposit / Withdraw:** Manage account balance  
- **Search Accounts:** By account ID or customer name

---

## Project Structure

```
bank-management-python/
├── LICENSE
├── README.md
├── requirements.txt
├── database.db
├── main.py
├── bank/
│ ├── init.py
│ ├── account.py
│ └── db.py
└── tests/
└── test_bank.py
```

---

## Database File
- The application uses **SQLite** to store account data.  
- A database file called `database.db` is **created automatically** in the same folder as `main.py` when you first run the program.  
- You **do not need to create it manually**.  

### Recommended `.gitignore` entries
