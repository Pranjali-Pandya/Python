
def date_timefunction():

    print("\nDate and Time\n")

    import datetime
    import time

    while(True):

        print("1. Display current date and time")
        print("2. Calculate the difference between two dates/time")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Exit")

        c = int(input("Enter your choice "))

        if c == 1:

            current = datetime.datetime.now()
            print("The current date and time is ", current)

            print("Year ", current.year)
            print("Month:", current.month)
            print("Day:", current.day)
            print("Hour:", current.hour)
            print("Minute:", current.minute)
            print("Second:", current.second)

        elif c == 2:

            print("1 Difference between date")
            print("2 Difference between time")

            ch = int(input("Enter your choice: "))

            if ch == 1:

                try:
                    date1 = input("Enter the date1 (DD/MM/YYYY) ")
                    date2 = input("Enter the date2 (DD/MM/YYYY) ")

                    formated_date1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
                    formated_date2 = datetime.datetime.strptime(date2, "%d/%m/%Y")

                    difference_date = formated_date2 - formated_date1

                    print("Difference")
                    print("Days ", difference_date.days)

                except ValueError:
                    print("Enter the valid date format")

            elif ch == 2:

                try:
                    time1 = input("Enter the date1 (HH:MM:SS) ")
                    time2 = input("Enter the date2 (HH:MM:SS) ")

                    formated_time1 = datetime.datetime.strptime(time1, "%H:%M:%S")
                    formated_time2 = datetime.datetime.strptime(time2, "%H:%M:%S")

                    difference_time = formated_time2 - formated_time1
                    difference_time = difference_time.seconds

                    print("Difference")
                    print("Hours: ", difference_time // 3600)
                    print("Minutes: ", (difference_time % 3600) // 60)
                    print("Seconds: ", (difference_time % 60))

                except ValueError:
                    print("Enter the Valid Time according to the format")

            else:
                print("Enter the valid option")

        elif c == 3:

            current = datetime.datetime.now()

            print("Format 1", current.strftime("%d-%m-%Y %H:%M:%S"))
            print("Format 2", current.strftime("%m-%d-%Y"))
            print("Format 3", current.strftime("%Y-%m-%d"))
            print("Format 4", current.strftime("%A, %d %B %Y"))
            print("Format 5", current.strftime("%d %B %Y"))

        elif c == 4:

            print("\n----------------------- Stop Watch------------------------------\n")

            start_timing = 0
            stop_timing = 0

            while(True):

                print("1 Start")
                print("2 Stop")
                print("3 Reset")
                print("4 Exit")

                ch = int(input("Enter your choice "))

                if ch == 1:

                    current = datetime.datetime.now()
                    start_timing = current
                    print("Start timing ", start_timing)

                elif ch == 2:

                    if start_timing != 0:

                        current2 = datetime.datetime.now()
                        stop_timing = current2

                        print("Your stop timing ", stop_timing)

                        difference = stop_timing - start_timing
                        total_seconds = difference.seconds

                        print("Difference")
                        print("Hours: ", total_seconds // 3600)
                        print("Minutes: ", (total_seconds % 3600) // 60)
                        print("Seconds: ", (total_seconds % 60))

                elif ch == 3:

                    start_timing = 0
                    stop_timing = 0
                    print("Stopwatch reset successfully")

                elif ch == 4:

                    print("\n---------------Thankyou for using stopwatch-------------------\n")
                    break

                else:
                    print("Invalid option")

        elif c == 5:

            print("\n---------------Countdown-----------------------\n")

            print("1. For minutes")
            print("2. For seconds")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                min = int(input("Enter the minutes: "))
                min_to_sec = min * 60
                total_seconds = min_to_sec

                while(total_seconds > 0):

                    current = time.time()

                    print("Time left : ", end="")
                    print("Time Left:", time.strftime("%M:%S", time.gmtime(total_seconds)))

                    time.sleep(1)
                    total_seconds -= 1

                print("Time Left: 00:00")

            elif choice == 2:

                sec = int(input("Enter the seconds: "))
                total_seconds = sec

                while(total_seconds >= 0):

                    current = time.time()

                    print("Time Left:", time.strftime("%M:%S", time.gmtime(total_seconds)))

                    time.sleep(1)
                    total_seconds -= 1

                print("STOP")

            else:
                print("Invalid option")

        elif c == 6:

            print("------------------Thankyou For Using datetime module-----------------------")
            break

        else:
            print("Invalid Option")
            
if __name__ == "__main__":
    print("Inside package running")
    date_timefunction() 
