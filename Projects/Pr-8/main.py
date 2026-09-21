import numpy as np


class DataAnalyst:

    # Constructor
    def __init__(self, array=None):
        self.__array = array

    # 1D Array class method
    @classmethod
    def create_1D(cls):
        values = list(map(float, input(
            "Enter elements separated by space: "
        ).split()))

        return cls(np.array(values))

    # 2D Array class method
    @classmethod
    def create_2d(cls):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        values = list(map(float, input(
            f"Enter {rows * cols} elements separated by space: "
        ).split()))

        if len(values) != rows * cols:
            print("Invalid number of elements!")
            return None

        arr = np.array(values).reshape(rows, cols)

        return cls(arr)

    # 3D Array class method
    @classmethod
    def create_3d(cls):
        layers = int(input("Enter number of layers: "))
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        total = layers * rows * cols

        values = list(map(float, input(
            f"Enter {total} elements separated by space: "
        ).split()))

        if len(values) != total:
            print("Invalid number of elements!")
            return None

        arr = np.array(values).reshape(layers, rows, cols)

        return cls(arr)

    # Display method
    def display(self):
        print("\nCurrent Array\n")
        print(self.__array)

    # Indexing
    def indexing(self):
        self.display()

        if self.__array.ndim == 1:

            index = int(input("Enter index: "))

            print("Element:", self.__array[index])

        elif self.__array.ndim == 2:

            row = int(input("Enter row index: "))
            col = int(input("Enter column index: "))

            print("Element:", self.__array[row, col])

        else:

            layer = int(input("Enter layer index: "))
            row = int(input("Enter row index: "))
            col = int(input("Enter column index: "))

            print("Element:", self.__array[layer, row, col])

    # Slicing
    def slicing(self):
        self.display()

        if self.__array.ndim == 1:

            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))

            print("Sliced Array:")
            print(self.__array[start:end])

        elif self.__array.ndim == 2:

            row_range = input("Enter row range (start:end): ")
            col_range = input("Enter column range (start:end): ")

            r1, r2 = map(int, row_range.split(":"))
            c1, c2 = map(int, col_range.split(":"))

            print("Sliced Array:\n")
            print(self.__array[r1:r2, c1:c2])

        else:

            layer_range = input("Enter layer range (start:end): ")
            row_range = input("Enter row range (start:end): ")
            col_range = input("Enter column range (start:end): ")

            l1, l2 = map(int, layer_range.split(":"))
            r1, r2 = map(int, row_range.split(":"))
            c1, c2 = map(int, col_range.split(":"))

            print("Sliced Array:\n")
            print(self.__array[l1:l2, r1:r2, c1:c2])

    # Private method for creating second array
    def __get_second_array(self):

        shape = self.__array.shape

        print("Enter elements for the second array:")

        values = list(map(float, input().split()))

        if len(values) != self.__array.size:
            print("Incorrect number of elements.")
            return None

        return np.array(values).reshape(shape)

    # Private method for creating second matrix
    def __get_second_matrix(self):

        rows = int(input("Enter number of rows for second matrix: "))
        cols = int(input("Enter number of columns for second matrix: "))

        print(f"Enter {rows * cols} elements:")

        values = list(map(float, input().split()))

        if len(values) != rows * cols:
            print("Incorrect number of elements.")
            return None

        return np.array(values).reshape(rows, cols)

    # Mathematical operations
    def mathematical_operation(self):

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        p = int(input("Enter your choice: "))

        if p in [1, 2, 3, 4, 5, 6]:

            second = self.__get_second_array()

            if second is None:
                return

            print("\nSecond Array:")
            print(second)

        if p == 1:

            result = self.__array + second

            print("\nAddition:")
            print(result)

        elif p == 2:

            result = self.__array - second

            print("\nSubtraction:")
            print(result)

        elif p == 3:

            result = self.__array * second

            print("\nMultiplication:")
            print(result)

        elif p == 4:

            if np.any(second == 0):
                print("Division by zero is not allowed.")

            else:
                result = self.__array / second

                print("\nDivision:")
                print(result)

        elif p == 5:

            if self.__array.ndim != 2:
                print("Dot product requires a 2D array.")
                return

            second = self.__get_second_matrix()

            if second is None:
                return

            if self.__array.shape[1] != second.shape[0]:

                print("Dot product is not possible.")
                print(
                    "Columns of first matrix must equal "
                    "rows of second matrix."
                )

                return

            print("\nOriginal Matrix:")
            print(self.__array)

            print("\nSecond Matrix:")
            print(second)

            result = np.dot(self.__array, second)

            print("\nDot Product:")
            print(result)

        elif p == 6:

            if self.__array.ndim != 2:
                print("Matrix multiplication requires a 2D array.")
                return

            second = self.__get_second_matrix()

            if second is None:
                return

            if self.__array.shape[1] != second.shape[0]:

                print("Matrix multiplication is not possible.")
                print(
                    "Columns of first matrix must equal "
                    "rows of second matrix."
                )

                return

            print("\nOriginal Matrix:")
            print(self.__array)

            print("\nSecond Matrix:")
            print(second)

            result = np.matmul(self.__array, second)

            print("\nMatrix Multiplication:")
            print(result)

        else:

            print("Your choice is wrong.")
            return

    # Static method
    @staticmethod
    def show_title():
        print("NumPy Analyzer")

    # Search, Sort and Filter
    def search_sort_filter(self):

        print("1. To search a value")
        print("2. To sort the array")
        print("3. To filter the array")

        p = int(input("Enter your choice: "))

        # SEARCH
        if p == 1:

            value = float(input("Enter value to search: "))

            result = np.where(self.__array == value)

            if len(result[0]) == 0:

                print("Value not found.")

            else:

                print("Value found at index:")
                print(result)

        # SORT
        elif p == 2:

            print("\nOriginal Array:")
            print(self.__array)

            # 1D Array
            if self.__array.ndim == 1:

                print("""
Choose sorting option:
1. Ascending
2. Descending
""")

                choice = int(input("Enter your choice: "))

                if choice == 1:

                    result = np.sort(self.__array)

                elif choice == 2:

                    result = np.sort(self.__array)[::-1]

                else:

                    print("Invalid choice.")
                    return

                print("\nSorted Array:")
                print(result)

            # 2D Array
            elif self.__array.ndim == 2:

                print("\nChoose Sorting option")
                print("1. Column-wise Ascending")
                print("2. Column-wise Descending")
                print("3. Row-wise Ascending")
                print("4. Row-wise Descending")

                choice = int(input("Enter your choice: "))

                if choice == 1:

                    result = np.sort(self.__array, axis=0)

                elif choice == 2:

                    result = np.sort(self.__array, axis=0)
                    result = np.flip(result, axis=0)

                elif choice == 3:

                    result = np.sort(self.__array, axis=1)

                elif choice == 4:

                    result = np.sort(self.__array, axis=1)
                    result = np.flip(result, axis=1)

                else:

                    print("Invalid choice.")
                    return

                print("\nSorted Array:")
                print(result)

            # 3D Array
            elif self.__array.ndim == 3:

                print("Choose sorting option")
                print("1. Axis 0 Ascending")
                print("2. Axis 0 Descending")
                print("3. Axis 1 Ascending")
                print("4. Axis 1 Descending")
                print("5. Axis 2 Ascending")
                print("6. Axis 2 Descending")

                choice = int(input("Enter your choice: "))

                if choice == 1:

                    result = np.sort(self.__array, axis=0)

                elif choice == 2:

                    result = np.sort(self.__array, axis=0)
                    result = np.flip(result, axis=0)

                elif choice == 3:

                    result = np.sort(self.__array, axis=1)

                elif choice == 4:

                    result = np.sort(self.__array, axis=1)
                    result = np.flip(result, axis=1)

                elif choice == 5:

                    result = np.sort(self.__array, axis=2)

                elif choice == 6:

                    result = np.sort(self.__array, axis=2)
                    result = np.flip(result, axis=2)

                else:

                    print("Invalid choice.")
                    return

                print("\nSorted Array:")
                print(result)

        # FILTER
        elif p == 3:

            value = float(input("Enter value: "))

            result = self.__array[self.__array > value]

            print("\nOriginal Array:")
            print(self.__array)

            print(f"\nValues greater than {value}:")
            print(result)

        else:

            print("Your choice is wrong.")

    # Aggregates
    def aggregates(self):

        print("\nOriginal Array:")
        print(self.__array)

        print("\nChoose an option:")

        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("Sum:", np.sum(self.__array))

        elif choice == 2:

            print("Mean:", np.mean(self.__array))

        elif choice == 3:

            print("Median:", np.median(self.__array))

        elif choice == 4:

            print("Standard Deviation:", np.std(self.__array))

        elif choice == 5:

            print("Variance:", np.var(self.__array))

        elif choice == 6:

            print("Minimum:", np.min(self.__array))

        elif choice == 7:

            print("Maximum:", np.max(self.__array))

        elif choice == 8:

            p = float(input("Enter percentile (0-100): "))

            if p < 0 or p > 100:

                print("Percentile must be between 0 and 100.")
                return

            print(
                f"{p}th Percentile:",
                np.percentile(self.__array, p)
            )

        elif choice == 9:

            second = self.__get_second_array()

            if second is None:
                return

            correlation = np.corrcoef(
                self.__array.flatten(),
                second.flatten()
            )[0, 1]

            print("Correlation Coefficient:", correlation)

        else:

            print("Invalid choice!")

    # Combine and Split
    def combine_split(self):

        print("\nOriginal Array:")
        print(self.__array)

        print("\nChoose an option:")

        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        # COMBINE
        if choice == 1:

            second = self.__get_second_array()

            if second is None:
                return

            print("\nSecond Array:")
            print(second)

            # 1D Array
            if self.__array.ndim == 1:

                result = np.concatenate(
                    (self.__array, second)
                )

                print("\nCombined Array:")
                print(result)

            # 2D Array
            elif self.__array.ndim == 2:

                print("\nChoose combine option:")

                print("1. Vertical Combine")
                print("2. Horizontal Combine")

                option = int(input("Enter your choice: "))

                if option == 1:

                    result = np.vstack(
                        (self.__array, second)
                    )

                    print("\nVertically Combined Array:")
                    print(result)

                elif option == 2:

                    result = np.hstack(
                        (self.__array, second)
                    )

                    print("\nHorizontally Combined Array:")
                    print(result)

                else:

                    print("Invalid choice.")

            # 3D Array
            elif self.__array.ndim == 3:

                print("\nChoose axis for combining:")

                print("1. Axis 0")
                print("2. Axis 1")
                print("3. Axis 2")

                axis = int(input("Enter your choice: ")) - 1

                if axis not in [0, 1, 2]:

                    print("Invalid axis.")
                    return

                result = np.concatenate(
                    (self.__array, second),
                    axis=axis
                )

                print("\nCombined Array:")
                print(result)

        # SPLIT
        elif choice == 2:

            # 1D Array
            if self.__array.ndim == 1:

                parts = int(input("Enter number of parts: "))

                if parts <= 0:

                    print("Invalid number of parts.")
                    return

                result = np.array_split(
                    self.__array,
                    parts
                )

                print("\nSplit Arrays:")

                for i, part in enumerate(result, 1):

                    print(f"Part {i}:")
                    print(part)

            # 2D Array
            elif self.__array.ndim == 2:

                print("\nChoose split option:")

                print("1. Split along rows")
                print("2. Split along columns")

                option = int(input("Enter your choice: "))

                parts = int(input("Enter number of parts: "))

                if parts <= 0:

                    print("Invalid number of parts.")
                    return

                if option == 1:

                    result = np.array_split(
                        self.__array,
                        parts,
                        axis=0
                    )

                elif option == 2:

                    result = np.array_split(
                        self.__array,
                        parts,
                        axis=1
                    )

                else:

                    print("Invalid choice.")
                    return

                print("\nSplit Arrays:")

                for i, part in enumerate(result, 1):

                    print(f"Part {i}:")
                    print(part)

            # 3D Array
            elif self.__array.ndim == 3:

                print("\nChoose split axis:")

                print("1. Axis 0")
                print("2. Axis 1")
                print("3. Axis 2")

                axis = int(input("Enter your choice: ")) - 1

                if axis not in [0, 1, 2]:

                    print("Invalid axis.")
                    return

                parts = int(input("Enter number of parts: "))

                if parts <= 0:

                    print("Invalid number of parts.")
                    return

                result = np.array_split(
                    self.__array,
                    parts,
                    axis=axis
                )

                print("\nSplit Arrays:")

                for i, part in enumerate(result, 1):

                    print(f"Part {i}:")
                    print(part)

        else:

            print("Invalid choice.")


# ============================================================
# MAIN PROGRAM
# ============================================================

print("Welcome to the NumPy Analyzer!")
print("=================================\n")

analyzer = None

while True:

    print("Choose an option:")
    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    try:

        choice = int(input("Enter your choice: "))

    except ValueError:

        print("Please enter a number from 1 to 6.")
        continue

    # OPTION 1
    if choice == 1:

        print("\nCreate a NumPy Array\n")

        print("Select the type of array you want to create")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        try:

            ch = int(input("Enter your choice: "))

        except ValueError:

            print("Please enter a number from 1 to 3.")
            continue

        if ch == 1:

            print("\nWrite the elements to be filled in 1D Array")

            analyzer = DataAnalyst.create_1D()

        elif ch == 2:

            analyzer = DataAnalyst.create_2d()

        elif ch == 3:

            analyzer = DataAnalyst.create_3d()

        else:

            print("Invalid Choice")
            continue

        # If array was created successfully
        if analyzer is not None:

            print("\nArray created successfully!")

            analyzer.display()

            # INDEXING AND SLICING MENU
            while True:

                print("\nChoose an option:")
                print("1. Accessing index in the array")
                print("2. Slicing in the array")
                print("3. Exit")

                try:

                    c = int(input("Enter your choice: "))

                except ValueError:

                    print("Please enter a number from 1 to 3.")
                    continue

                if c == 1:

                    analyzer.indexing()

                elif c == 2:

                    analyzer.slicing()

                elif c == 3:

                    break

                else:

                    print("Invalid Choice")

    # OPTION 2
    elif choice == 2:

        print("\nPerform Mathematical Operations")

        if analyzer is None:

            print("Please create an array first.")

        else:

            analyzer.mathematical_operation()

    # OPTION 3
    elif choice == 3:

        print("\nCombine or Split Arrays")

        if analyzer is None:

            print("Please create an array first.")

        else:

            analyzer.combine_split()

    # OPTION 4
    elif choice == 4:

        print("\nSearch, Sort, or Filter Arrays")

        if analyzer is None:

            print("Please create an array first.")

        else:

            analyzer.search_sort_filter()

    # OPTION 5
    elif choice == 5:

        print("\nCompute Aggregates and Statistics")

        if analyzer is None:

            print("Please create an array first.")

        else:

            analyzer.aggregates()

    # OPTION 6
    elif choice == 6:

        print("\nThank you for using the NumPy Analyzer! Goodbye!")

        break

    # INVALID CHOICE
    else:

        print("\nInvalid choice! Please try again.")
