print("\n\n Welcome to Data Analyzer and Transformer Program \n\n")
arr = []
def input_data():
    """Input 1D or 2D array manually or use sample data"""
    global arr

    print("1. Enter to create an array manually")
    print("2. Enter to use a sample data")

    ch = int(input("Enter your choice "))

    if ch == 1:

        print("1. To enter 1D array")
        print("2. To enter 2D array")

        c = int(input("Enter your choice "))

        if c == 1:

            arr = [int(i) for i in input(
                "Enter the numbers seperated by (,): ").split(',')]
            print("\n Data has been stored successfully\n")

        elif c == 2:

            rows1 = int(input("Enter number of rows: "))
            arr = []

            for i in range(rows1):
                row = [int(i) for i in input(
                    f"Enter the elements for {i+1} seperated by (,): ").split(',')]
                arr.append(row)

            print("\n Data has been stored successfully\n")

        else:
            print("\nInvalid choice\n")

    elif ch == 2:

        print("1. Sample for 1D array")
        print("2. Sample for 2D array")

        c = int(input("Enter your choice "))

        if c == 1:

            arr = [23, 43, 12, 56, 78, 78, 90]
            print("\n Data will be successfully used\n")

        elif c == 2:

            arr = [
                [1, 3, 4],
                [23, 67, 34],
                [76, 12, 34],
                [90, 23, 12]
            ]

            print("\n Data will be successfully used\n")

        else:
            print("\nInvalid choice\n")

    else:
        print("\n\n Invalid choice \n")


def display_data_summary():
    """Display summary of dataset using built-in functions"""

    if len(arr) == 0:
        print("No array entered\n")

    elif type(arr[0]) == list:

        print("It is 2D array")

        for row in arr:
            print(row)

    else:

        print(arr)

        unique = []

        for i in arr:
            if i not in unique:
                unique.append(i)

        print("1. The length of array ", len(arr))
        print("2. The sum of elements of array ", sum(arr))
        print("3. The minimum number ", min(arr))
        print("4. The maximum number ", max(arr))
        print("5. The unique values ", unique)


def cal_factorial(n):
    """Calculate factorial of a number using recursion"""

    if n == 0:
        return 1
    elif n==0:
        return 0
    else:
        return n * cal_factorial(n - 1)


def filter_threshold(n):
    """Filter values greater than the given threshold using lambda and filter"""
    if len(arr) == 0:
        print("No array entered\n")

    elif type(arr[0]) == list:
        print("It is 2D array")
    else:
        
       filter_data = list(filter(lambda x: x > n, arr))
       print(filter_data)


def sort_data():
    """Sort 1D array using sort() and 2D array using sorted()"""

    if len(arr) == 0:
        print("No array entered\n")

    elif type(arr[0]) == list:

        new_sorted = sorted(arr)
        print("Sorted 2D array ", new_sorted)

    else:

        print("Choose sorting option:")
        print("1. Ascending Order")
        print("2. Descending Order")

        c = int(input("Enter your choice: "))

        if c == 1:

            arr.sort()
            print("The sorted array in ascending order: ", arr)

        elif c == 2:

            arr.sort(reverse=True)
            print("The sorted array in descending order: ", arr)

        else:
            print("Your choice is incorrect")


def display_statistics():
    """Return minimum, average, maximum and total of the dataset"""

    if len(arr) == 0:
        print("No array entered\n")
        return None, None,None,None

    elif type(arr[0]) == list:
        print("It is 2D array")
        return None, None,None,None

    else:
        return min(arr), sum(arr)/len(arr), max(arr), sum(arr)


def display_data_args(*args):

    for i in args:
        print(i)


while True:

    print("1. Input Data")
    print("2. Display Data Summary (Built in Function)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Variable)")
    print("7. Display Dataset")
    print("8. Exit Program")

    choice = int(input("Please enter your choice: "))

    if choice == 1:

        input_data()

    elif choice == 2:

        display_data_summary()

    elif choice == 3:

        num = int(input("Enter the number to calculate factorial: "))
        fact = cal_factorial(num)

        print(fact)

    elif choice == 4:

        threshold = int(
            input("Enter a threshold value to filter out data above this value "))
        filter_threshold(threshold)

    elif choice == 5:

        sort_data()

    elif choice == 6:

        minimum, average, maximum, Total = display_statistics()
        if minimum == None and average ==None and  maximum == None and Total == None:
            pass
        else:
           print("The minimum value ", minimum)
           print("The average value ", average)
           print("The maximum value ", maximum)
           print("The Sum of all elements of array ", Total)

    elif choice == 7:

        display_data_args(*arr)

    elif choice == 8:

        print("\n*********** Thankyou for using Data Analyzer and Transformer Program ***************\n")
        break

    else:

        print("Invalid choice")
