def file_module():
    print("\n******************* Welcome to a Personal Journal Manager *********************\n")


    class JournalManager:

        def create_file(self):
            try:
                with open("journal.txt", "x"):
                    print("\nFile created successfully")
            except FileExistsError:
                print("\nFile already exists")

        def add_entry(self):

            class InvalidDateError(Exception):
                pass

            date = input("\nEnter the current date (DD/MM/YYYY): ")

            try:
                if len(date) != 10 or date[2] != '/' or date[5] != '/':
                    raise InvalidDateError

                day = int(date[0:2])
                month = int(date[3:5])
                year = int(date[6:])

                if day < 1 or day > 31:
                    raise InvalidDateError

                if month < 1 or month > 12:
                    raise InvalidDateError

                if year <= 0:
                    raise InvalidDateError

            except (InvalidDateError, ValueError):
                print("Enter the date in correct format(DD/MM/YYYY)")
                return

            class InvalidTimeError(Exception):
                pass

            time = input("Enter the current time in 24 hrs format(12:04): ")

            try:
                if len(time) != 5 or time[2] != ':':
                    raise InvalidTimeError

                part1 = int(time[0:2])
                part2 = int(time[3:5])

                if part1 < 0 or part1 > 23:
                    raise InvalidTimeError

                if part2 < 0 or part2 > 59:
                    raise InvalidTimeError

            except (InvalidTimeError, ValueError):
                print("Enter the valid time")
                return

            entry = input("\nEnter journal entry:\n")

            with open("journal.txt", "a") as file:
                file.write(f"Date: {date} Time: {time}\n")
                file.write(entry + "\n\n")

            print("\nJournal entry added successfully\n")

        def view_entry(self):

            class EmptyFileError(Exception):
                pass

            try:
                with open("journal.txt", "r") as file2:
                    content = file2.read()

                    if not content:
                        raise EmptyFileError

                    print("\nYour Journal Entries:\n")
                    print("------------------------------------------------------")
                    print(content)

            except FileNotFoundError:
                print("File does not exist")

            except EmptyFileError:
                print("No Journal Entries Found")

        def search_entry(self):

            class EmptyFileError(Exception):
                pass

            try:
                with open("journal.txt", "r") as file2:
                    content = file2.read()

                    if not content:
                        raise EmptyFileError

                    search = input(
                        "Enter the date, time or the keyword as per your entry only: "
                    )

                    entry = content.split("\n\n")
                    found = False

                    for ent in entry:
                        if search.lower() in ent.lower():
                            print("\nMatching entry")
                            print("-------------------------------------------------------")
                            print(ent + "\n")
                            found = True

                    if found == False:
                        print("No Matching Entry Found")

            except FileNotFoundError:
                print("File does not exist")

            except EmptyFileError:
                print("No Journal Entries Found")

        def delete_entry(self):

            class EmptyFileError(Exception):
                pass

            try:
                with open("journal.txt", "r") as file2:
                    content = file2.read()

                if not content:
                    raise EmptyFileError

                c = input("Are you sure you want to delete? (Yes/No): ")

                if c == "Yes":
                    with open("journal.txt", "w") as file:
                        file.write("")

                    print("\nAll Journal entries removed successfully.")

                else:
                    print("Delete Cancelled")

            except FileNotFoundError:
                print("No journal file existing")
                return

            except EmptyFileError:
                print("File is already empty")
                return

    obj = JournalManager()

    while True:

        print("\n1. Create a Journal File")
        print("2. Add a New Entry")
        print("3. View all Entry")
        print("4. Search for an Entry")
        print("5. Delete All Entries")
        print("6. To exit\n")

        try:
            ch = int(input("Enter your choice: "))

        except ValueError:
            print("Enter valid Number")
            continue

        if ch == 1:
            obj.create_file()

        elif ch == 2:
            obj.add_entry()

        elif ch == 3:
            obj.view_entry()

        elif ch == 4:
            obj.search_entry()

        elif ch == 5:
            obj.delete_entry()

        elif ch == 6:
            print("\n******************* Thankyou for Using Personal Journal Manager ********************")
            break

        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    print("Inside package running")
    file_module()
 
