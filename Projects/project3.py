print("**************** Welcome to Student Data Organizer ******************** \n\n")

student = {}
st_list = []

while (True):
    print("1. Add student")
    print("2. Display all students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subject Offered")
    print("6. Exit ")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        id = int(input("Enter student id:  "))
        found = False

        for student in st_list:
            if student["ID"] == id:
                found = True
                break

        if found == True:
            print("Student ID already exists")

        else:
            st_name = input("Enter student name : ")
            age = int(input("Enter student age : "))
            grade = input("Enter student grade : ")
            dob = input("Enter date of birth(DD-MM-YYYY) : ")

            if len(dob) != 10 or dob[2] != '-' or dob[5] != '-':
                print("Inavalid date of birth")
                continue

            subject = input("Enter the subjects : ")
            subject2 = subject.split(",")  # converts list to string

            st_tuple = (id, dob)

            sb_set = set()

            for s in subject2:
                sb_set.add(s)

            student = {
                "ID": st_tuple[0],
                "Name": st_name,
                "Age": age,
                "Date Of Birth ": st_tuple[1],
                "Grade": grade,
                "Subject": sb_set
            }

            st_list.append(student)
            print("\n Student added successfully\n")

    elif choice == 2:
        if not st_list:
            print("No student records available")
        else:
            print("\n*********************All students are*******************\n")

            for item in st_list:
                subject3 = ",".join(item['Subject'])
                print(f"Id {item['ID']} | Name {item['Name']} | Age {item['Age']} | Date Of Birth {item['Date Of Birth ']} | Grade {item['Grade']} | Subject {subject3} ")

    elif choice == 3:
        if not st_list:
            print("No student records available")

        else:
            id = int(input("Enter id to update "))
            found = False

            for student in st_list:
                if student["ID"] == id:
                    print("Enter what you want to update ")
                    print("1. Name you want to update ")
                    print("2. Age you want to update ")
                    print("3. Grade you want to update ")
                    print("4. Subjects you want to update ")

                    c = int(input("Enter your choice"))

                    if c == 1:
                        n = input("Enter student name ")
                        student["Name"] = n
                        print("Updated Successfully")

                    elif c == 2:
                        a = int(input("Enter the age "))
                        student["Age"] = a
                        print("Updated Successfully")

                    elif c == 3:
                        g = a = input("Enter the grade ")
                        student["Grade"] = g
                        print("Updated Successfully")

                    elif c == 4:
                        sub = input("Enter the subject you want to update seperated by commas ")
                        student["Subject"] = set(sub.split(","))
                        print("Updated Successfully")

                    else:
                        print("Incorrect choice")

                    found = True
                    break

            if found == False:
                print("Id not found")

    elif choice == 4:
        if not st_list:
            print("No student record available")

        else:
            id = int(input("Enter id to delete"))
            found = False

            for i in range(len(st_list)):
                if st_list[i]["ID"] == id:
                    del st_list[i]
                    print("Student id deleted")
                    found = True
                    break

            if found == False:
                print("ID is wrong")

    elif choice == 5:
        if not st_list:
            print("No student record available")

        else:
            allsubjects = set()

            for student in st_list:
                allsubjects.update(student["Subject"])

            print("All subjects are ", allsubjects)

    else:
        print("\n\n********************Thankyou for using Student Data Organizer***********************\n\n")
        break
