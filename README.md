# Bank System

Rudimentary bank system implemented in Python for APU python module assignment. Text-based user interface and basic banking functionalities, designed to run in terminal.

## Features

- **Different User Types**: Superuser, Admins, and Customers. Superuser hardcoded.
- **Account Management**: Superuser can manage Admins. Superuser and Admins can manage Customers.
- **Account Applications**: Admins can review and approve/reject Customer account applications.
- **Transactions**: Deposits, withdrawals, generating account statements.
- **Login System**: Basic username-password authentication system.
- **Data Persistence**: Admin and Customer details stored in text files.

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

### Usage

1. **Run in terminal**:
   ```bash
   python bank_system.py
   ```

   **OR**

2. **Load bank_system.py in any python supported environment**

### Instructions

- **Superuser login**:
   - Username: superuser
   - Password: 123
- **Default Admin login**
   - Username: admin
   - Password: 123
- **Default Customer**
   - Username: customer
   - Password: 123
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

