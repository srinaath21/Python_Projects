import mysql.connector as mysql

db = mysql.connect(host="localhost", user='root', password="", database="college")
command_handler = db.cursor(buffered=True)


def student_session(user_name):
    while 1:
        print("\n1. View Register")
        print("2. Download Register")
        print("3. Logout")

        user_opt = input("Option: ")
        if user_opt == '1':
            username = (str(user_name),)
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s", username)
            records = command_handler.fetchone()
            for record in records:
                for _ in record:
                    record.strip("'")
                    record.strip(",")
                    record.strip("(")
                    record.strip(")")
                print(record, end=" ")
        elif user_opt == '2':
            print("Downloading Register...")
            username = (str(user_name),)
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s", username)
            records = command_handler.fetchall()
            record_list = list(records[0])
            for record in record_list:
                record.strip("'")
                record.replace(",", " -")
                with open("Register.txt", "w") as f:
                    f.write(str(record_list) + '\n')
                f.close()
            print("All records saved successfully")

        elif user_opt == '3':
            print("Loging Out")
            break
        else:
            print("Invalid Input")


def teacher_session():
    while 1:
        print("")
        print("Teacher Menu")
        print("1. Mark student register")
        print("2. View student register")
        print("3. Logout")

        user_opt = input("Option: ")
        if user_opt == '1':
            print("\nMark Student Register")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = command_handler.fetchall()
            date = input("Dates: DD/MM/YYYY : ")
            for record in records:
                record = str(record).replace("'", "")
                record = str(record).replace(",", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                # Present | Absent | Late
                status = input(f"Status for {str(record)} P/A/L : ").upper()
                query_vals = (str(record), date, status)
                command_handler.execute("INSERT INTO attendance (username, date, status) VALUES (%s, %s, %s)",
                                        query_vals)
                db.commit()
                print(f"{record} marked as {status} ")
        elif user_opt == '2':
            command_handler.execute("SELECT date, username, status FROM attendance")
            records = command_handler.fetchall()
            print("\nDisplaying Student Register")
            for record in records:
                record = str(record).replace("'", "")
                record = str(record).replace(",", " -")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                print(record)
        elif user_opt == '3':
            print("\nLoging Out")
            break
        else:
            print("\nInvalid Input")


def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register New Student")
        print("2. Register New Teacher")
        print("3. View Students list")
        print("4. View Teachers list")
        print("5. Delete Existing Student")
        print("6. Delete Existing Teacher")
        print("7. Logout")

        user_opt = input("Option: ")
        if user_opt == '1':
            print("\nRegister new Student")
            username = input("Student username: ").capitalize()
            password = input("Password: ")
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users(username, password, privilege) VALUES (%s, %s, 'student')",
                                    query_vals)
            db.commit()
            print(f"{username} has been registered as Student")

        elif user_opt == '2':
            print("\nRegister new Teacher")
            username = input("Teacher username: ").capitalize()
            password = input("Password: ")
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users(username, password, privilege) VALUES (%s, %s, 'teacher')",
                                    query_vals)
            db.commit()
            print(f"{username} has been registered as Teacher")

        elif user_opt == '3':
            print("\nViewing Students List")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = command_handler.fetchall()
            for i in range(len(records)):
                for record in records[i]:
                    record.strip("'")
                    record.strip(",")
                    record.strip("(")
                    record.strip(")")
                    print(record)

        elif user_opt == '4':
            print("\nViewing Teachers List")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'teacher'")
            records = command_handler.fetchall()
            for i in range(len(records)):
                for record in records[i]:
                    record.strip("'")
                    record.strip(",")
                    record.strip("(")
                    record.strip(")")
                    print(record)

        elif user_opt == '5':
            print("\nDelete Existing Student Account")
            username = input("Student username: ").capitalize()
            query_vals = (username, "student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ", query_vals
                                    )
            db.commit()
            if command_handler.rowcount < 1:
                print("User Not Found!")
            else:
                print(f"{username} has been deleted.")

        elif user_opt == '6':
            print("\nDelete Existing Teacher Account")
            username = input("Teacher username: ").capitalize()
            query_vals = (username, "teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User Not Found!")
            else:
                print(f"{username} has been deleted.")

        elif user_opt == '7':
            print("Loging Out")
            break
        else:
            print("Invalid Input")


def auth_student():
    print("\nStudent's Login")
    username = input("Username: ")
    password = input("Password: ")
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'student'",
                            query_vals)
    username = command_handler.fetchone()
    username = (username[1].strip("'"))
    print(username)
    if command_handler.rowcount <= 0:
        print("Login Not Recognized")
    else:
        student_session(username)


def auth_teacher():
    print("\nTeachers Login\n")
    username = input("Teacher username: ")
    password = input("Password: ")
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'",
                            query_vals)
    if command_handler.rowcount <= 0:
        print("Login not recognized")
    else:
        teacher_session()


def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = str(input("Username: "))
    password = str(input("Password: "))
    if username.casefold() == 'admin':
        if password == '123':
            admin_session()
        else:
            print("Incorrect Password")
    else:
        print("Login details not recognized")


def main():
    while 1:
        print("\nWelcome to College System")
        print("")
        print("1. Login as Student")
        print("2. Login as Teacher")
        print("3. Login as Admin")
        print("4. Exit")

        user_choice = str(input("Option: "))
        if user_choice == '1':
            auth_student()
        elif user_choice == '2':
            auth_teacher()
        elif user_choice == '3':
            auth_admin()
        elif user_choice == '4':
            exit(0)
        else:
            print("Wrong Choice")


main()
