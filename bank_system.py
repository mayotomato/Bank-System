import datetime

# controls:
accept = 'y'
cancel = 'n'
goback = 'q'

superuser = ["superuser", "123"]
# admins are stored in admins.txt
# customers are stored in the format CUSTOMERINFO_[customerusername].txt

current = {
    "MYR": "100",
    "USD": "20",
    "EUR": "20",
}

savings = {
    "MYR": "500",
    "USD": "150",
    "EUR": "100",
}


"""
    File Overwriting Function
"""
def overwrite(accountName, password, id, name, type, passportNID, DOB, phoneNumber, address, currency, bal,
              first_time_login):
    accountDetails = ["PASSWORD: " + password + '\n',
                      "ACCOUNT ID: " + id + '\n',
                      "ACCOUNT NAME: " + name + '\n',
                      "ACCOUNT TYPE: " + type + '\n',
                      "PASSPORT ID: " + passportNID + '\n',
                      "DATE OF BIRTH: " + DOB + "\n",
                      "PHONE NUMBER: " + phoneNumber + "\n",
                      "ADDRESS: " + address + "\n",
                      "CURRENCY: " + currency + '\n',
                      "CURRENT BALANCE: " + str(bal) + '\n'
                      "\nfirst time login: " + first_time_login + "\n"

                      "\n----------TRANSACTION HISTORY-----------\n\n",]
    for i in TransactionInfo(accountName):
        accountDetails.append(i)


    with open('CUSTOMERINFO_' + accountName + ".txt", "w") as file:
        for i in accountDetails:
            file.write(i)
    return accountDetails


"""
    Login and Registration Functions
"""
# Registration form and account opening
def Registration():
    data = []
    # Personal details
    print("Welcome to Bank of Feline registration")
    print("Personal Information")
    name = input("Name: ")
    data.append(name)
    nid = input("NID/Passport No.: ")
    data.append(nid)
    # Check valid date
    while True:
        dob = input("Date of Birth (dd/mm/yyyy): ")
        try:
            datetime.datetime.strptime(dob, "%d/%m/%Y")
        except:
            print("Invalid date, try again")
            continue
        break
    data.append(dob)
    address = input("Current Address: ")
    data.append(address)
    phone = input("Phone number: ")
    data.append(phone)

    # Account details
    print("\nAccount information")

    # username creation
    while True:
        with open("Usernames.txt", "r") as text:
            files = text.readlines()
            checkfiles = []
            for x in files:
                z = x.strip("\n")
                checkfiles.append(z)

            username = input("Choose a username: ")
            while len(username) < 3:
                username = input("Username must be at least 3 characters, try again: ")
            if username in checkfiles:
                print("Username already exists choose a new username")
                continue
            else:
                with open("Usernames.txt", "a") as file:
                    file.write(username + "\n")
                break

    data.append(username)
    # Check correct account type entered
    while True:
        acc_type = input("Account type (Savings/Current): ").capitalize()
        if acc_type == "Savings":
            type = savings
            break
        elif acc_type == "Current":
            type = current
            break
        else:
            print("Invalid account type chosen, please choose (Savings/Current): ")
    data.append(acc_type)
    # Check correct currency entered
    while True:
        currency = input("Currency (MYR/USD/EUR): ").upper().strip()
        if currency == "MYR" or currency == "USD" or currency == "EUR":
            break
        else:
            print("Invalid currency chosen, please choose (MYR/USD/EUR): ")
    data.append(currency)
    # Check correct deposit entered
    while True:
        try:
            deposit = int(input("Deposit (Must be at least {} {} ): ".format(type[currency], currency)))
            if deposit >= int(type[currency]):
                break
            else:
                print("Insufficient deposit (Must be at least {} {} ): ".format(type[currency], currency))
        except:
            print("Enter a valid number")
            continue
    data.append(str(deposit))

    # Application text file creation
    with open("Applications.txt", "a") as customer:
        customer.write("%".join(data))
        customer.write("\n")

    print("\nYou can login after any admin opens your account.\n")
    return


#---login function
def loginPage():
    print("\n\n---LOGIN PAGE---\n")
    while True:

        # [Login or create account]

        # prompt user
        print("Please login to continue... (Enter 'q' to cancel)")
        usernameInput = input("USERNAME: ")
        # if usernameInput = q go back to introduction screen, new usernames cannot be less than 3 characters anyway
        if usernameInput.lower() == "q":
            return ["q", "q"]

        passwordInput = input("PASSWORD: ").strip()


        # check if the admin exists. if it doesn't, move on
        with open("admins.txt", "r") as file:
            contents = [line.strip().split(",") for line in file]
            for i in contents:
                if usernameInput == i[0]:
                    if passwordInput == i[1]:
                        return [i[0], "admin"]

        if usernameInput == superuser[0]:
            if passwordInput == superuser[1]:
                return ["YNAYNA", "SUPER_USER"]

        # check if the account exists. if it doesn't raise error
        try:
            file = open('CUSTOMERINFO_' + usernameInput + ".txt", "r")
            accountDetails = file.readlines()

            # check if password matches
            if passwordInput == accountDetails[0].replace('PASSWORD: ', '').replace('\n', ''):
                print("\n\n ~Successfully logged in!~")
                return [usernameInput, 'customer']

            # if it doesn't, raise error
            else:
                raise NameError()
        except:
            print("\nSorry, your credentials are invalid.")


"""
    Main Menu Functions
"""
#---CUSTOMER MAIN MENU
def customerMainMenu(account, details):
    customerMainMenuOptions = {
        '1': "Deposit",
        '2': "Withdrawal",
        '3': "Generate Account Report",
        '4': "Settings",
        '5': "Support",
        '6': "Logout"
    }

    print("\n\n---MAIN MENU PAGE---\n")
    print("Welcome, " + account + ". How may we help you?\n")

    # spits out all account details
    for i in details[1:10]:
        print(i.strip("\n"))
    print()

    while True:
        # prints out the list of options
        for i in customerMainMenuOptions:
            print(i + ". " + customerMainMenuOptions[i])
        print()

        # prompt user
        choice = input("Please select from the menu: ")

        # validation check
        try:
            if choice in customerMainMenuOptions:
                return choice
            else:
                raise ValueError()
        except:
            print("\nThat choice is invalid. Please try again. ")


#---ADMIN MAIN MENU
def adminMainMenu(accountname):
    AdminMainMenuOptions = {
        '1': "Change Customer Details",
        '2': "Generate Account Statements",
        '3': "Open Account",
        '4': "Logout"
    }

    print("\n\n---ADMIN MAIN MENU PAGE---\n")
    print("Welcome, " + accountname + ". get working!! \n")

    while True:
        # prints out the list of options
        for i in AdminMainMenuOptions:
            print(i + ". " + AdminMainMenuOptions[i])
        print()

        # prompt user
        choice = input("Please select from the menu: ")

        # validation check
        try:
            if choice in AdminMainMenuOptions:
                return choice
            else:
                raise ValueError()
        except:
            print("\nThat choice is invalid. Please try again. ")


#---SUPER USER MAIN MENU
def SuperuserMainMenu(accountname):
    SuperuserMainMenuOptions = {
        '1': "Change Customer Details",
        '2': "Generate Account Statements",
        '3': "Add/remove admins",
        '4': "Open Account",
        '5': 'Log out'
    }

    print("\n\n---SUPERUSER MAIN MENU PAGE---\n")
    print("WELCOME, " + accountname + ". COMMAND US. GUIDE US. \n")

    while True:
        # prints out the list of options
        for i in SuperuserMainMenuOptions:
            print(i + ". " + SuperuserMainMenuOptions[i])
        print()

        # prompt user
        choice = input("Please select from the menu: ")

        # validation check
        try:
            if choice in SuperuserMainMenuOptions:
                return choice
            else:
                raise ValueError()
        except:
            print("\nThat choice is invalid. Please try again. ")


'''
    Universal Functions
'''

#---show current usernames function
def showcurrentusernames():
    check = []
    with open("Usernames.txt", "r") as customers:
        lines = customers.readlines()
        for count, line in enumerate(lines):
            line = line.strip()
            print("{}. ".format(count + 1) + line)
            check.append(line)
    print("")
    return check

#---show current admins function
def showcurrentadmins(choice):
    adminlist = []
    passwordlist = []
    with open("admins.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line != "\n":
                adminlist.append(line.split(',')[0])
                passwordlist.append(line.split(',')[1].strip())

    # return clean admin list
    file.close()
    if choice == "adminlist":
        return adminlist

    # or return lines from admin.txt
    if choice == "lines":
        return lines

    # or print out admin list with formatting
    if choice == "print":
        print("Current admins: ")
        for count, admin in enumerate(adminlist):
            print(f"{str(count + 1)}. Username: {admin} Password: {passwordlist[count]}")


#---account report generator function
def Statement(username):
    datelist = []
    try:
        transactions = TransactionInfo(username)
        print("Dates of activity:")
        print("0. CANCEL")
        for count, transaction in enumerate(transactions):
            y = transaction.split(", ")
            datelist.append(y[0])
            print(f"{count+1}. {y[0]}")

        # Choose end date and start date, user given option to choose corresponding number
        start_date = input("\nChoose number from list or enter starting date (dd/mm/yyyy): ").strip()
        if start_date == "0":
            return
        if start_date.isdigit():
            start_date = datelist[int(start_date)-1]
        end_date = input("Choose number from list or enter ending date (dd/mm/yyyy): ").strip()
        if end_date == "0":
            return
        if end_date.isdigit():
            end_date = datelist[int(end_date)-1]

        # Empty string used to signify no limit
        if start_date == "" and end_date == "":
            print("")
            return "".join(transactions)

        # No limit on start date but specific end date with validation
        elif start_date == "" and (end_date in datelist):
            end_index = datelist.index(end_date)
            report = transactions[:end_index + 1]
            print("")
            return "".join(report)

        # Specific start date but no limit on end date with validation
        elif (start_date in datelist) and end_date == "":
            start_index = datelist.index(start_date)
            report = transactions[start_index:]
            print("")
            return "".join(report)
        elif (start_date in datelist) and (end_date in datelist):
            start_index = datelist.index(start_date)
            end_index = datelist.index(end_date)

            # Return statement within specified range
            report = transactions[start_index:end_index + 1]
            print("")
            return "".join(report)

        else:
            return "Invalid dates"

    except SyntaxError:
        # Invalid user returned if admin user searched wrong username
        return "Invalid username"


##---read transaction history
def TransactionInfo(username):
    with open("CUSTOMERINFO_" + username + ".txt", "r") as file:
        lines = file.readlines()
        index = lines.index("----------TRANSACTION HISTORY-----------\n")
        transactions = lines[index + 2:]
        return transactions


##---update with new transactions
def updateTransaction(transactiontype, amount, currency, username):
    lines_before_transaction_history = []

    current_date = datetime.datetime.now().strftime("%d/%m/%Y").lstrip("0").replace("/0", "/")

    with open("CUSTOMERINFO_" + username + ".txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            lines_before_transaction_history.append(line)
            if line.strip() == "----------TRANSACTION HISTORY-----------":
                break

    start_index = lines.index("----------TRANSACTION HISTORY-----------\n") + 1
    transaction_history = lines[start_index:]

    flag = 1
    with open("CUSTOMERINFO_" + username + ".txt", 'w') as new_file:

        # writing first part
        for line in lines_before_transaction_history:
            new_file.write(line)

        # splitting to get date and comparing with current date
        for line in transaction_history:
            parts = line.strip().split(', ')
            date = parts[0]

            if date == current_date:
                flag = 0
                if transactiontype == "w":
                    appendline = line.strip() + ", Withdrawal - " + str(amount) + " " + currency + "\n"
                elif transactiontype == "d":
                    appendline = line.strip() + ", Deposit - " + str(amount) + " " + currency + "\n"

                new_file.write(appendline)
            else:
                new_file.write(line)
    new_file.close()

    # new date
    if (flag == 1):
        with open("CUSTOMERINFO_" + username + ".txt", "w") as new_file:
            if transactiontype == "w":
                appendline = current_date + ", Withdrawal - " + str(amount) + " " + currency + "\n"
            elif transactiontype == "d":
                appendline = current_date + ", Deposit - " + str(amount) + " " + currency + "\n"

            lines.append(appendline)
            for line in lines:
                new_file.write(line)


##---change pass
def change_pass(accountName, password, nid, name, type, passportNID, DOB, phoneNumber, address, currency, bal,
                first_time_login):
    first_time_login = first_time_login.strip()

    # prompt first time password change
    if first_time_login == "yes":
        newpass0 = ""
        newpass1 = "."

        # confirming
        while newpass0 != newpass1:
            newpass0 = input("This is your first time logging in, please set up a new password: ")
            newpass1 = input("Confirm new password: ")

        # updating file
        overwrite(accountName, newpass0, nid, name, type, passportNID, DOB, phoneNumber, address, currency, bal,
                  "no")
        first_time_login = "no"
        print("Password changed successfully!")

    # password change if not first time
    elif first_time_login == "no":
        while True:
            checkpass = input("Enter your current password: ")
            if checkpass == password:
                break
            else:
                print("Incorrect password")
        while True:

            # password checking
            if checkpass == password:
                newpass2 = input("Enter new password: ")
                newpass3 = input("Confirm new password: ")
                if newpass2 == password:
                    print("New password cannot be old password")
                    continue
                elif newpass2 != password and newpass2 == newpass3:
                    overwrite(accountName, newpass2, nid, name, type, passportNID, DOB, phoneNumber, address, currency, bal,
                          "no")
                    print("Password changed successfully!")
                    break
                else:
                    print("Passwords did not match try again")


'''
    Customer Functions
'''
#---DEPOSIT PAGE
def depositPage(currency, bal, username):
    while True:
        print("\n\n---DEPOSIT PAGE---\n")

        # show current balance
        print("Current Balance: " + str(bal) + ' ' + currency)

        # prompt user for value to deposit
        while True:
            while True:
                try:
                    choice = input("\nHow much would you like to deposit? Press 'q' to go back\nPlease enter a value: ")
                    if choice == goback:
                        print("\nGoing back to main menu...")
                        return bal
                    intchoice = int(choice)
                    if intchoice <= 0:
                        print("\nThat value is below zero. Please try again")
                        break
                    else:
                        depositValue = intchoice
                except:
                    print("\nThat value is invalid. Please try again")
                    break

                while True:
                    choice = input("\nConfirm the deposit (y/n): ")
                    if choice == accept:
                        # go and add balance
                        bal += depositValue
                        print("\nDEPOSIT CONFIRMED.")
                        print("Current Balance: " + str(bal) + ' ' + currency)


                        transactiontype = "d"
                        updateTransaction(transactiontype, depositValue, currency, username)
                        return bal
                    elif choice == cancel or choice == goback:
                        depositValue = 0
                        print("\nCancelled deposit.")
                        break
                    else:
                        # invalid choice
                        print("\nThat choice is invalid. Please try again. ")


#---DEPOSIT PAGE
def withdrawalPage(currency, bal, minBalance, username):
    while True:
        print("\n\n---WITHDRAWAL PAGE---\n")

        # show current balance
        print("Current Balance: " + str(bal) + ' ' + currency)

        # prompt user for value to deposit
        while True:
            while True:
                try:
                    choice = input("\nHow much would you like to withdraw? Press 'q' to go back\nPlease enter a value: ")
                    if choice == goback:
                        print("\nGoing back to main menu...")
                        return bal
                    intchoice = int(choice)
                    if intchoice <= 0:
                        print("\nThat value is below zero. Please try again")
                        break
                    if (bal - intchoice) < minBalance:
                        print("\nYou cannot withdraw more than the minimum balance. Please try again")
                        break
                    else:
                        withdrawValue = intchoice
                except:
                    print("\nThat value is invalid. Please try again")
                    break

                while True:
                    choice = input("\nConfirm the withdrawal (y/n): ")
                    if choice == accept:
                        # go and add balance
                        bal -= withdrawValue
                        print("\nWITHDRAWAL CONFIRMED.")
                        print("Current Balance: " + str(bal) + ' ' + currency)
                        transactiontype = "w"
                        updateTransaction(transactiontype, withdrawValue, currency, username)

                        return bal
                    elif choice == cancel or choice == goback:
                        withdrawValue = 0
                        print("\nCancelled withdrawal.")
                        break
                    else:
                        # invalid choice
                        print("\nThat choice is invalid. Please try again. ")


def settingsPage():
    settingsMenuOptions = {
        '1': "Change Password",
        '2': "Return to Menu???"
    }

    print("\n\n---SETTINGS PAGE---\n")

    while True:

        # prints out the list of options
        for i in settingsMenuOptions:
            print(i + ". " + settingsMenuOptions[i])
        print()

        # prompt user
        choice = input("Please select from the menu: ")

        # validation check
        try:
            if choice in settingsMenuOptions:
                return choice
            else:
                raise ValueError()
        except:
            print("\nThat choice is invalid. Please try again. ")


def supportPage():
    print("\n\n---SUPPORT PAGE---\n")
    print("For help, please contact this number:\n02498394435")
    choice = input("\nPress any key to exit to main menu: ")


'''
    Admin & Super user Functions
'''
#---account Creation function##
def OpenAcc():
    try:
        # Data processing
        with open("Applications.txt", "r") as customer:
            data = customer.readlines()
            if len(data) == 0:
                raise ValueError()
    except:
        print("\nNo applications available.\n")
        return

    print("\n\nAccount Approval\n")
    for z, acc in enumerate(data):
        account = acc.split("%")

        print("Account number {}\n".format(z + 1))
        print("Username: ", account[5])
        print("Name: ", account[0])
        print("Passport ID: ", account[1])
        print("D.O.B: ", account[2])
        print("Current Address: ", account[3])
        print("Phone Number: ", account[4])
        print("Account type: ", account[6])
        print("Currency: ", account[7])
        print("Deposit: " + account[8].strip() + " " + account[7].strip())
        process = input("\nApprove this application? (Yes/No/Quit): ")

        if process.lower() == "y" or process.lower() == "yes":

            # Generate account number
            now = datetime.datetime.today()
            acc_no = str(now.day // 9) + str(now.hour // 9) + str(now.minute // 9) + str(now.second // 9) + str(
                now.microsecond // 9) + str(now.microsecond // 999)

            # Generate default passord
            defaultpassword = ""
            for x, num in enumerate(acc_no):
                if x % 2 == 0:
                    defaultpassword += chr(int(num) % 26 + 64)
                else:
                    defaultpassword += chr(int(num) % 26 + 97)
                if x == 3:
                    defaultpassword += "!"

            defaultpassword = str(defaultpassword)

            # Additional account setup
            first_time_login = "yes"
            balance = 0
            balance += int(account[8])

            # Approved account text file creation
            with open("CUSTOMERINFO_" + account[5] + ".txt", "w") as customer:
                customer.write(
                    "PASSWORD: " + defaultpassword + "\n" +
                    "ACCOUNT ID: " + acc_no + '\n' +
                    "ACCOUNT NAME: " + account[0] + '\n' +
                    "ACCOUNT TYPE: " + account[6] + '\n' +
                    "PASSPORT ID: " + account[1] + '\n' +
                    "DATE OF BIRTH: " + account[2] + "\n" +
                    "PHONE NUMBER: " + account[4] + "\n" +
                    "ADDRESS: " + account[3] + "\n" +
                    "CURRENCY: " + account[7] + '\n' +
                    "CURRENT BALANCE: " + str(balance) + '\n' +
                    "\nfirst time login: " + first_time_login + "\n" +

                    "\n----------TRANSACTION HISTORY-----------\n\n")

            # Delete line
            with open("Applications.txt", "r") as file:
                lines = file.readlines()
            with open("Applications.txt", "w") as file:
                for line in lines:
                    if line != acc:
                        file.write(line)
            print("The users default password is: " + defaultpassword)
        elif process.lower() == "n" or process.lower() == "no":

            # Delete line
            with open("Applications.txt", "r") as file:
                lines = file.readlines()
            with open("Applications.txt", "w") as file:
                for line in lines:
                    if line != acc:
                        file.write(line)

            # Update Usernames.txt
            with open("Usernames.txt", "r") as fil:
                users = fil.readlines()
                print(users)
                print(account[5])
            with open("Usernames.txt", "w") as fil:
                users.remove(account[5] + "\n")
                for user in users:
                    fil.write(user)
    return

def ChangeCustomerDetails(username):
    with open("CUSTOMERINFO_" + username + ".txt", "r+") as customer:
        lines = customer.readlines()

        #Stores CUSTOMERINFO_username.txt without formatting
        changedlines = []
        print("Username: ",username)
        print("Choose line")
        print("0. CANCEL")
        line = lines[0]
        count = 0
        line = line.strip()
        changedlines.append(line)
        print("{}. ".format(count+1) + line)

        # print usernames
        for count,line in enumerate(lines[4:8]):
            line = line.strip()
            changedlines.append(line)
            print("{}. ".format(count+2) + line)


        strippedchangedlines = []
        fields = []
        for p in changedlines:
            line = p.split(": ")
            fields.append(line[0]+": ")
            strippedchangedlines.append(line[1])

        print("")
        choice = input("Choose line to change: ")

        # 0 to cancel
        if choice == "0":
            return

        # 1 change password
        elif choice == "1":
            newpassword = input("Enter new password: ")
            strippedchangedlines[0] = newpassword

        # 2 new passport id
        elif choice == "2":
            newpassportid = input("Enter new passport ID: ")
            strippedchangedlines[1] = newpassportid

        # 3 update dob with validation
        elif choice == "3":
            while True:
                newdob = input("Date of Birth (dd/mm/yyyy): ")
                try:
                    datetime.datetime.strptime(newdob, "%d/%m/%Y")
                except:
                    print("Invalid date, try again")
                    continue
                break
            strippedchangedlines[2] = newdob

        # 4 new phone number
        elif choice == "4":
            newphone = input("Enter new phone number: ")
            strippedchangedlines[3] = newphone

        # 5 new address
        elif choice == "5":
            newaddress = input("Enter new address: ")
            strippedchangedlines[4] = newaddress

        # updating lines from CUSTOMERINFO_ file
        lines[0] = fields[0] + strippedchangedlines[0] + "\n"
        lines[4] = fields[1] + strippedchangedlines[1] + "\n"
        lines[5] = fields[2] + strippedchangedlines[2] + "\n"
        lines[6] = fields[3] + strippedchangedlines[3] + "\n"
        lines[7] = fields[4] + strippedchangedlines[4] + "\n"

        print("\nDetail changed successfully!")

    # writing back updated lines into CUSTOMERINFO_ file
    with open("CUSTOMERINFO_" + username + ".txt", "w") as customer:
        for a in lines:
            customer.write(a)

'''
    Flow functions
'''
def customerFlow(accountname):
    while True:

        # reads file, transfers info into array, then into variables (for better readability)
        with open('CUSTOMERINFO_' + accountname + '.txt', 'r') as file:
            accountDetails = file.readlines()
        password = accountDetails[0].replace("PASSWORD: ", '')
        password = password.replace('\n', '')
        accountID = accountDetails[1].replace("ACCOUNT ID: ", '')
        accountID = accountID.replace('\n', '')
        name = accountDetails[2].replace("ACCOUNT NAME: ", '')
        name = name.replace('\n', '')
        accountType = accountDetails[3].replace("ACCOUNT TYPE: ", '')
        accountType = accountType.replace('\n', '')
        passportNID = accountDetails[4].replace("PASSPORT ID: ", '')
        passportNID = passportNID.replace('\n', '')
        DOB = accountDetails[5].replace("DATE OF BIRTH: ", '')
        DOB = DOB.replace('\n', '')
        phoneNumber = accountDetails[6].replace("PHONE NUMBER: ", '')
        phoneNumber = phoneNumber.replace('\n', '')
        address = accountDetails[7].replace("ADDRESS: ", '')
        address = address.replace('\n', '')
        currency = accountDetails[8].replace("CURRENCY: ", '')
        currency = currency.replace('\n', '')
        balance = accountDetails[9].replace("CURRENT BALANCE: ", '')
        balance = balance.strip()
        balance = int(balance)
        first_time_login = accountDetails[11].replace("first time login: ", '')
        first_time_login = first_time_login.replace('\n', '')

        if accountType == 'Current':
            minBalance = int(current[currency])
        else:
            minBalance = int(savings[currency])

        if first_time_login == "yes":
            change_pass(accountname, password, accountID, name, accountType, passportNID, DOB,
                        phoneNumber, address, currency, balance, first_time_login)
            continue
        elif first_time_login == "no":
            choice = customerMainMenu(accountname, accountDetails)


        # interpreting user choice
        match choice:
            # DEPOSIT PAGE
            case '1':
                accountDetails = overwrite(accountname, password, accountID, name, accountType,
                                           passportNID, DOB, phoneNumber, address, currency,
                                           depositPage(currency, balance,accountname), first_time_login)
            # WITHDRAWAL PAGE
            case '2':
                accountDetails = overwrite(accountname, password, accountID, name, accountType,
                                           passportNID, DOB, phoneNumber, address, currency,
                                           withdrawalPage(currency, balance, minBalance, accountname), first_time_login)
            # GENERATE STATEMENTS
            case '3':
                print(Statement(accountname))

            # SETTINGS PAGE
            case '4':
                if settingsPage() == '1':
                    change_pass(accountname, password, accountID, name, accountType, passportNID, DOB,
                                phoneNumber, address, currency, balance, first_time_login)

            # SUPPORT PAGE
            case '5':
                supportPage()

            # LOG OUT
            case '6':
                break


def adminFlow(accountname):
    while True:
        # launch main menu
        choice = adminMainMenu(accountname)

        # interpreting user choice
        match choice:

            # CHANGE CUSTOMER DETAILS
            case '1':
                while True:
                    print("\nChoose customer to change details of: ")
                    print("0. CANCEL")
                    check = showcurrentusernames()
                    username = input("Please enter customer username or choose number from the list: ")
                    try:
                        if username == "0":
                            break
                        ChangeCustomerDetails(check[int(username) - 1])
                    except IndexError:
                        print(f"Customer number {username} does not exist!")
                        continue
                    except ValueError:
                        if username in check:
                            ChangeCustomerDetails(username)
                            break
                        else:
                            print(f"Customer {username} does not exist!")
                            continue

        # ACCOUNT STATEMENT GENERATION
            case '2':
                # while True:
                #     username = input("\nPlease enter customer username: ")
                #     try:
                #         open("CUSTOMERINFO_" + username + ".txt", "r")
                #     except:
                #         print("Customer doesn't exist. Please try again.")
                #     break
                # print(Statement(username))
                while True:
                    print("\nChoose customer to generate statement of: ")
                    print("0. CANCEL")
                    check = showcurrentusernames()
                    username = input("Please enter customer username or choose number from the list: ")
                    try:
                        if username == "0":
                            break
                        print(Statement(check[int(username) - 1]))
                    except IndexError:
                        print(f"Customer number {username} does not exist!")
                        continue
                    except ValueError:
                        if username in check:
                            print(Statement(username))
                            break
                        else:
                            print(f"Customer {username} does not exist!")
                            continue

            # Open account
            case '3':
                OpenAcc()

            # LOG OUT
            case '4':
                break


def superuserFlow(accountname):
    while True:
        # launch main menu
        choice = SuperuserMainMenu(accountname)

        # interpreting user choice
        match choice:

            # CHANGE CUSTOMER DETAILS
            case '1':
                while True:
                    print("\nChoose customer to change details of: ")
                    print("0. CANCEL")
                    check = showcurrentusernames()
                    username = input("Please enter customer username or choose number from the list: ")
                    try:
                        if username == "0":
                            break
                        ChangeCustomerDetails(check[int(username) - 1])
                    except IndexError:
                        print(f"Customer number {username} does not exist!")
                        continue
                    except ValueError:
                        if username in check:
                            ChangeCustomerDetails(username)
                            break
                        else:
                            print(f"Customer {username} does not exist!")
                            continue

            # ACCOUNT STATEMENT GENERATION
            case '2':
                while True:
                    print("\nChoose customer to generate statement of: ")
                    print("0. CANCEL")
                    check = showcurrentusernames()
                    username = input("Please enter customer username or choose number from the list: ")
                    try:
                        if username == "0":
                            break
                        print(Statement(check[int(username) - 1]))
                    except IndexError:
                        print(f"Customer number {username} does not exist!")
                        continue
                    except ValueError:
                        if username in check:
                            print(Statement(username))
                            break
                        else:
                            print(f"Customer {username} does not exist!")
                            continue

                # print(Statement(username))

        # ADMIN MANAGEMENT
            case '3':
                while True:
                    # List of admins
                    adminlist = showcurrentadmins("adminlist")

                    # Puts current admins on screen
                    showcurrentadmins("print")
                    print("\nWould you like to\n1.Create new admin\n2.Delete existing admin\n3.Exit to menu")
                    adminmanagementchoice = input("\nEnter choice: ")

                    # Create new admin
                    if (adminmanagementchoice == '1'):
                        newadmin = input("\nEnter new admin username: ")
                        if (newadmin in adminlist):
                            print("\nAdmin " + newadmin + " already exists!\n")
                        if len(newadmin) < 3:
                            print("Admin username cannot be under 3 characters")
                        else:
                            newpass = input("\nEnter password for new admin: ")
                            with open("admins.txt", "a") as file:
                                file.write("\n" + newadmin + "," + newpass)
                                print("\nAdmin " + newadmin + " added successfully!\n")

                            file.close()

                    # Delete admin from system
                    elif (adminmanagementchoice == '2'):
                        showcurrentadmins("print")
                        deladmin = input("\nEnter username of admin to delete: ")
                        if (deladmin in adminlist):
                            updated_adminlist = []
                            lines = showcurrentadmins("lines")
                            for line in lines:
                                if not line.startswith(deladmin + ','):
                                    updated_adminlist.append(line)
                            lines = updated_adminlist

                            if "\n" in lines[-1]:
                                lines[-1] = lines[-1].strip()

                            with open("admins.txt", "w") as frewrite:
                                for line in lines:
                                    frewrite.write(line)
                            frewrite.close()
                            print("\nAdmin " + deladmin + " terminated.\n")

                        else:
                            print("\nAdmin " + deladmin + " does not exist!\n")
                    # Go back
                    elif (adminmanagementchoice == '3'):
                        break
                    else:
                        print("\nInvalid choice")

            # Open account
            case '4':
                OpenAcc()

            # Log out
            case '5':
                break



'''
    MAIN
'''
def main():
    while True:
        # 1. show introduction screen
        print("\n\n  ╱|、\n(˚ˎ 。7  \n|、˜〵          \nじしˍ,)ノ Bank of Feline introduction screen /ᐠ - ˕ -マ Ⳋ")

        #2. ask registration or login
        while True:
            print("\n1.Log in\n2.Apply for registration\n3.Exit program")
            choice = input("\nPlease select from the menu: ").strip()
            if choice == '1':
                # . show login page
                currentSessionAccount = loginPage()

                # redirect to flows
                if currentSessionAccount[1] == "customer":  # if currentSessionAccount is customer, defer to customer() function
                    customerFlow(currentSessionAccount[0])
                elif currentSessionAccount[1] == "admin":  # if currentSessionAccount is admin, defer to admin() function
                    adminFlow(currentSessionAccount[0])
                elif currentSessionAccount[1] == "SUPER_USER":  # if currentSessionAccount is superuser, defer to superuser() function
                    superuserFlow(currentSessionAccount[0])
                else:
                    break

            elif choice == '2':
                Registration()

            elif choice == '3':
                print("Ciao!")
                return

            else:
                print("\nInvalid input. Please try again.")


if __name__ == "__main__":
    main()

