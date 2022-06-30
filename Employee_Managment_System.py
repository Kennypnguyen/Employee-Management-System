# Employee Managment System

# Import modules
from os import system
import re
import mysql.connector

# Making connection
connection = mysql.connector.connect(host = "localhost", user = "root", password = "KennyNguyen7", database = "employee")

# Create a table in MySQL, once the system is first runned, these two lines of code need to be commented out because table has been created in database

# mycursor = connection.cursor()
# mycursor.execute("CREATE TABLE employeedata (Id INT(11) PRIMARY KEY, Name VARCHAR(1800), Email_id TEXT(1800), Phone_no BIGINT (11), Address TEXT(1000), Salary BIGINT(20))")

# make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# for validating an Phone Number
pattern = re.compile("(0|91)?[7-9][0-9]{9}")

# Function to add employees 
def add_employee():
    print("{:>60}".format("*** Add Employee Record ***"))
    print("\n")
    id = input("Enter employee ID: ")
    # Check if employee ID already exists 
    if(check_employee(id) == True):
        print("Employee Id already exists\nPlease try again")
        press = input("Press any key to continue")
        add_employee()
    name = input("Enter employee name: ")
    # Check if employee name already exists
    if(check_employee_name(name) == True):
        print("Employee name already exists\nPlease try again")
        press = input("Press any key to continue")
        add_employee()
    email_id = input("Enter employee email ID: ")
    # Check if employee email ID valid
    if(re.fullmatch(regex, email_id)):
        print("Valid email")
    else:
        print("Invalid email")
        press = input("Press any key to continue")
        add_employee()
    phone_no = input("Enter employee phone number: ")
    # Check if phone number is valid
    if(pattern.match(phone_no)):
        print("Valid phone number")
    else:
        print("Invalid phone number")
        press = input("Press any key to continue")
        add_employee()
    address = input("Enter employee address: ")
    salary = input("Enter employee salary: ")
    data = (id, name, email_id, phone_no, address, salary)
    # Insert employee data in the employee (employeedata) table
    sql = 'insert into employeedata values(%s, %s, %s, %s, %s, %s)'
    c = connection.cursor()

    # Execute the sql query
    c.execute(sql, data)

    # Use commit() method to make changes in the table
    connection.commit()
    print("Sucessfully added employee record")
    press = input("Press any key to continue")
    menu()

# Define methods that check to see if either employee's name or ID already exists
def check_employee(employee_id):
    # query to select all rows from employee(employeedata) table
    sql = 'select * from employeedata where Id=%s'
    # Making cursor buffered to make row count method work properly 
    c = connection.cursor(buffered = True)
    data = (employee_id,)
    # Execute the sql query
    c.execute(sql, data)
    # rowcount method to find number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def check_employee_name(employee_name):
    # query to select all rows from employee(employeedata) table
    sql = 'select * from employeedata where Id=%s'
    # Making cursor buffered to make row count method work properly 
    c = connection.cursor(buffered = True)
    data = (employee_name,)
    # Execute the sql query
    c.execute(sql, data)
    # rowcount method to find number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Method to display employee record
def display_employee():
    print("{:>60}".format("*** Display Employee Record ***"))
    print("\n")
    # query to select all rows from employee (employeedata) table
    sql = 'select * from employeedata'
    c = connection.cursor()
    # Executing the sql query
    c.execute(sql)
    # Fetching all details of all employees
    r = c.fetchall()
    for i in r:
        print("Employee ID: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email ID: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Salary: ", i[5])
        print("\n")
    press = input("Press any key to continue")
    menu()

# Method to update employee record
def update_employee():
    print("{:>60}".format("*** Update Employee Record ***"))
    print("\n")
    id = input("Enter employee ID you would like to update: ")
    # Check to see if employee ID exists 
    if(check_employee(id) == False):
        print("Employee record does not exists\n Try again")
        press = input("Press any key to continue")
        update_employee()
    else:
        print("\nWhich feature did you want to update?: ")
        print("1. Update employee email")
        print("2. Update employee phone number")
        print("3. Update employee address")
        print("4. Return to menu")
        print("{:>60}".format("*** Choice Options: [1|2|3|4] ***"))
        print("\n")
        choice = int(input("Enter your choice: "))
        # Choice 1 would update the employee email
        if(choice == 1):
            email_id = input("Enter updated employee email ID: ")
            if(re.fullmatch(regex, email_id)):
                print("Valid email")
            else:
                print("Invalid email")
                press = input("Press any key to continue")
                update_employee()
            # Update email_id 
            sql = 'UPDATE employeedata set Email_Id = %s'
            data = (email_id,)
            c = connection.cursor()
            # Execute the sql query
            c.execute(sql, data)
            # commit() method to make changes in the table
            connection.commit()
            print("Updated employee email ID")
            press = input("Press any key to continue")
            menu()
        # Choice 2 would update employee phone number
        if(choice == 2):
            phone_no = input("Enter updated employee phone number: ")
            if(pattern.match(phone_no)):
                print("Valid phone number")
            else:
                print("Invalid phone number")
                press = input("Press any key to continue")
                update_employee()
            # Update phone_no
            sql = 'UPDATE employeedata set Phone_no = %s'
            data = (phone_no,)
            c = connection.cursor()
            # Execute the sql query
            c.execute(sql, data)
            # commit() method to make changes in the table
            connection.commit()
            print("Updated employee phone number")
            press = input("Press any key to continue")
            menu()
        # Choice 3 would update the employee address
        if(choice == 3):
            address = input("Enter updated employee address: ")
            # Update address
            sql = 'UPDATE employeedata set Address = %s'
            data = (address,)
            c = connection.cursor()
            # Execute the sql query
            c.execute(sql, data)
            # commit() method to make changes in the table
            connection.commit()
            print("Updated employee address")
            press = input("Press any key to continue")
            menu() 
        if(choice == 4):
            print("Returning to menu")
            menu()  
        else: 
            print("Invalid choice")
            press = input("Press any key to continue")
            update_employee()
    

# Method to promote employee's salary
def promote_employee():
    print("{:>60}".format("*** Promote Employee ***"))
    print("\n")
    id = input("Enter employee ID you would like to promote: ")
    # Check to see if employee ID exists 
    if(check_employee(id) == False):
        print("Employee record does not exists\n Try again")
        press = input("Press any key to continue")
        promote_employee()
    else:
        amount = int(input("Enter increased salary: "))
        # query to fetch salary of employee with given data
        sql = 'select Salary from employeedata where Id=%s'
        data = (id,)
        c = connection.cursor()
        # executing the sql query
        c.execute(sql, data)
        # fetching salary of employee with given ID
        r = c.fetchone()
        t = r[0] + amount
        # query to update salary of employee with given ID
        sql = 'update employeedata set Salary = %s where Id = %s'
        d = (t, id)
        # executing the sql query
        c.execute(sql, d)
        #commmit() method to make changes in the table
        connection.commit()
        print("Employee promoted")
        press = input("Press any key to continue")
        menu()

# Method to remove employee from system
def remove_employee():
    print("{:>60}".format("*** Remove Employee ***"))
    print("\n")
    id = input("Enter employee ID you would like to promote: ")
    # Check to see if employee ID exists 
    if(check_employee(id) == False):
        print("Employee record does not exists\n Try again")
        press = input("Press any key to continue")
        remove_employee()
    else:
        # query to delete employee from employeedata table
        sql = 'delete from employeedata where Id = %s'
        data = (id,)
        c = connection.cursor()
        # executing the sql query
        c.execute(sql, data) 
        # commit method to make changes to employeedata table
        connection.commit()
        print("Employee removed")
        press = input("Press any key to continue")
        menu()

# Method to search for an employee from the system
def search_employee():
    print("{:>60}".format("*** Search Employee ***"))
    print("\n")
    id = input("Enter employee ID you would like to promote: ")
    # Check to see if employee ID exists 
    if(check_employee(id) == False):
        print("Employee record does not exists\n Try again")
        press = input("Press any key to continue")
        search_employee()
    else:
        print("\nEmployee found: \n")
        # query to search employee from employeedata table
        sql = 'select * from employeedata where Id = %s'
        data = (id,)
        c = connection.cursor()
        # executing the sql query
        c.execute(sql, data)
        # fetch all details of the employee
        r = c.fetchall()
        for i in r:
            print("Employee ID: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email ID: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Salary: ", i[5])
            print("\n")
        press = input("Press any key to continue.")
        menu()

# Menu method to display main menu of the employee managment system
def menu():
    system("cls")
    print("{:>60}".format("**********************************"))
    print("{:>60}".format("*** Employee Management System ***"))
    print("{:>60}".format("**********************************"))
    print("\n")
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee")
    print("5. Remove Employee")
    print("6. Search Employee")
    print("7. Exit\n")
    print("{:>60}".format("*** Choice Options: [1|2|3|4|5|6|7] ***"))
    print("\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        system("cls")
        add_employee()
    elif choice == 2:
        system("cls")
        display_employee()
    elif choice == 3:
        system("cls")
        update_employee()
    elif choice == 4:
        system("cls")
        promote_employee()
    elif choice == 5:
        system("cls")
        remove_employee()
    elif choice == 6:
        system("cls")
        search_employee()
    elif choice == 7:
        system("cls")
        print("{:>60}7".format("Have a nice day"))
        exit(0)
    else:
        print("Invalid Choice")
        press = input("Press any key To continue")
        menu()

# Call menu function
menu()