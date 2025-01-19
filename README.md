# Bank System

Rudimentary bank system implemented in Python to practice programming concepts. Text-based user interface and basic banking functionalities, designed to run in terminal.

## Features

- **Different User Types**: Superuser, Admins, and Users. Superuser hardcoded.
- **Account Management**: Superuser can manage Admins. Superuser and Admins can manage Users.
- **Account Applications**: Admins can review and approve/reject User account applications.
- **Transactions**: Deposits, withdrawals, generating account statements.
- **Login System**: Basic username-password authentication system.
- **Data Persistence**: Admin and User details stored in text files.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone Repository**:
   ```bash
   git clone https://github.com/mayotomato/Bank-System.git
   ```

**OR**

1. **Download ZIP File**:
      - Click "Download ZIP" under the Code button
      - Extract the downloaded file.

2. **Navigate to the project directory**:
   ```bash
   cd Bank-System
   ```

### Usage

1. **Run in terminal**:
   ```bash
   python bank_system.py
   ```

   **OR**

2. **Run in any Python-supported IDE by loading bank_system.py**

### Instructions

- **Superuser login**:
   Username: superuser
   Password: 123
- **Default Admin login**
   Username: admin
   Password: 123
- **Default User**
   Username: customer
   Password: 123
- **Creating Customer**
   - Apply for registration
   - Enter valid details
   - Approve customer application through admin/superuser under "Open Customer Account" (Possible to reject)
   - Default first time password generated in next line.
   - Copy default first time password.
   - Login to customer with password.
   - Set a password as it is first time logging in.
- **Creating Admin**
   - Login to superuser
   - Go to "Add/remove admins"
   - "Create new admin"
   - Enter details
---

## Disclaimer

This project is intended for learning and experimentation with programming concepts. It is not designed for production use. The login system is not secure, and data handling is limited to basic text file operations.
