print("\n\n********************Employee Management System***********************")

class Employee:
    def __init__(self, empid = None, name = None, age = None, salary = None):
        self.__empid = empid
        self.name = name
        self.age = age
        self.__salary = salary

    def set_info(self, empid):
        self.__empid = empid

    def get_info(self):
        return self.__empid

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def display(self):
        print("The employee details are as follows:")
        print(f"Employee Id: {self.__empid} Name: {self.name} Age: {self.age} Salary: {self.__salary}")

    def __del__(self):
        print("Employee Class Destroyed")


class Manager(Employee):
    def __init__(self, empid, name, age, salary, department):
        super().__init__(empid, name, age, salary)
        self.department = department

    def display(self):
        print("The Manager details are as follows")
        print(f"Employee Id: {self.get_info()} Name: {self.name} Age: {self.age} Salary: {self.get_salary()} Department: {self.department}")

    def __del__(self):
        print("Manager Class Destroyed")


class Developer(Employee):
    def __init__(self, empid, name, age, salary, prog_lang):
        super().__init__(empid, name, age, salary)
        self.prog_lang = prog_lang

    def display(self):
        print("The Developer details are as follows")
        print(f"Employee Id: {self.get_info()} Name: {self.name} Age: {self.age} Salary: {self.get_salary()} Programming Language: {self.prog_lang}")

    def __del__(self):
        print("Developer Class Destroyed")


emp = []
dev = []
man = []

while True:
    print("\n1. Add Employee")
    print("2. Add View Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Check Subclass")
    print("6. To exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("1. To Add Employee")
        print("2. To Add Manager")
        print("3. To Add Developer")

        c = int(input("Enter your choice: "))

        if c == 1:
            isexist = False
            emp_id = int(input("Enter the id of employee: "))

            for employee in emp:
                if employee.get_info() == emp_id:
                    isexist = True
                    break

            if isexist:
                print(f"{emp_id} of Employee already exist in the list")
            else:
                name = input("Enter the name of the employee ")
                age = int(input("Enter the age of employee: "))
                salary = int(input("Enter the salary of employee: "))

                obj1 = Employee(emp_id, name, age, salary)
                print("\nEmployee Created successfully!\n")
                emp.append(obj1)

        elif c == 2:
            isexist = False
            man_id = int(input("Enter the id of manager: "))

            for manager in man:
                if manager.get_info() == man_id:
                    isexist = True
                    break

            if isexist:
                print(f"{man_id} of Manager already exist in the list")
            else:
                name = input("Enter the name of the manager ")
                age = int(input("Enter the age of manager: "))
                salary = int(input("Enter the salary of manager: "))
                department = input("Enter the department of manager: ")

                obj2 = Manager(man_id, name, age, salary, department)
                print("\nManager Created successfully!\n")
                man.append(obj2)

        elif c == 3:
            isexist = False
            dev_id = int(input("Enter the id of developer: "))

            for developer in dev:
                if developer.get_info() == dev_id:
                    isexist = True
                    break

            if isexist:
                print(f"{dev_id} of Developer already exist in the list")
            else:
                name = input("Enter the name of the developer ")
                age = int(input("Enter the age of developer: "))
                salary = int(input("Enter the salary of developer: "))
                prog_lang = input("Enter the programming language of developer: ")

                obj3 = Developer(dev_id, name, age, salary, prog_lang)
                print("\nEmployee Created successfully!\n")
                dev.append(obj3)

        else:
            print("Invalid choice")

    elif ch == 2:
        print("1. To view Employee")
        print("2. To view Manager")
        print("3. To view Developer")

        c = int(input("Enter your choice: "))

        if c == 1:
            if len(emp) == 0:
                print("Nothing added in the list")
            else:
                for employee in emp:
                    employee.display()

        elif c == 2:
            if len(man) == 0:
                print("Nothing added in the list")
            else:
                for manager in man:
                    manager.display()

        elif c == 3:
            if len(dev) == 0:
                print("Nothing added in the list")
            else:
                for developer in dev:
                    developer.display()

        else:
            print("Invalid choice")

    elif ch == 3:
        print("1. To update Employee")
        print("2. To update Manager")
        print("3. To update Developer")

        c = int(input("Enter your choice: "))

        if c == 1:
            if len(emp) == 0:
                print("Nothing added in the list")
            else:
                eid = int(input("Enter the id you want to update: "))
                found = False

                for employee in emp:
                    if employee.get_info() == eid:
                        name = input("Enter the updated name ")
                        age = int(input("Enter new age: "))
                        salary = int(input("Enter new salary: "))

                        employee.name = name
                        employee.age = age
                        employee.set_salary(salary)
                        found = True
                        break

                if found:
                    print("\nEmployee Details updated successfully\n")
                else:
                    print(f"{eid} Id not found")

        elif c == 2:
            if len(man) == 0:
                print("Nothing added in the list")
            else:
                mid = int(input("Enter the manager id you want to update: "))
                found = False

                for manager in man:
                    if manager.get_info() == mid:
                        name = input("Enter updated name: ")
                        age = int(input("Enter updated age: "))
                        salary = int(input("Enter updated salary: "))
                        department = input("Enter updated department: ")

                        manager.name = name
                        manager.age = age
                        manager.set_salary(salary)
                        manager.department = department
                        found = True
                        break

                if found:
                    print("\nManager Details updated successfully\n")
                else:
                    print(f"{mid} Id not found")

        elif c == 3:
            if len(dev) == 0:
                print("Nothing added in the list")
            else:
                did = int(input("Enter the developer id you want to update: "))
                found = False

                for developer in dev:
                    if developer.get_info() == did:
                        name = input("Enter updated name: ")
                        age = int(input("Enter updated age: "))
                        salary = int(input("Enter updated salary: "))
                        prog_lang = input("Enter updated programming language: ")

                        developer.name = name
                        developer.age = age
                        developer.set_salary(salary)
                        developer.prog_lang = prog_lang
                        found = True
                        break

                if found:
                    print("\nDeveloper Details updated successfully\n")
                else:
                    print(f"{did} Id not found")

        else:
            print("Invalid choice")

    elif ch == 4:
        print("1. To Delete Employee")
        print("2. To Delete Manager")
        print("3. To Delete Developer")

        c = int(input("Enter your choice: "))

        if c == 1:
            if len(emp) == 0:
                print("Nothing added in the list to be deleted")
            else:
                eid = int(input("Enter the employee id you want to delete: "))
                found = False

                for employee in emp:
                    if employee.get_info() == eid:
                        emp.remove(employee)
                        found = True
                        break

                if found:
                    print("Employee removed successfully")
                else:
                    print(f"{eid} Id not found")

        elif c == 2:
            if len(man) == 0:
                print("Nothing added in the list to be deleted")
            else:
                mid = int(input("Enter the manager id you want to delete: "))
                found = False

                for manager in man:
                    if manager.get_info() == mid:
                        man.remove(manager)
                        found = True
                        break

                if found:
                    print("Manager removed successfully")
                else:
                    print(f"{mid} Id not found")

        elif c == 3:
            if len(dev) == 0:
                print("Nothing added in the list to be deleted")
            else:
                did = int(input("Enter the developer id you want to delete: "))
                found = False

                for developer in dev:
                    if developer.get_info() == did:
                        dev.remove(developer)
                        found = True
                        break

                if found:
                    print("Developer removed successfully")
                else:
                    print(f"{did} Id not found")

        else:
            print("Invalid choice")

    elif ch == 5:
        print("1. Check Manager subclass of Employee")
        print("2. Check Developer subclass of Employee")

        c = int(input("Enter your choice: "))

        if c == 1:
            print(issubclass(Manager, Employee))
        elif c == 2:
            print(issubclass(Developer, Employee))
        else:
            print("Invalid option")

    elif ch == 6:
        print("\nThank you for using Employee Management System\n")
        break

    else:
        print("Invalid choice")
