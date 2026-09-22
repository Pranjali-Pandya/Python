import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    # ==================================================
    # CONSTRUCTOR
    # ==================================================

    def __init__(self, data=None):
        self.data = data

    # ==================================================
    # DESTRUCTOR
    # ==================================================

    def __del__(self):
        pass

    # ==================================================
    # LOAD DATASET
    # ==================================================

    def load_data(self):

        try:

            self.data = pd.read_csv(
                "P:/Data Science/Jupyter Notebook 2/sales_data.csv"
            )

            print("\nDataset loaded successfully!")
            print("Number of rows:", self.data.shape[0])
            print("Number of columns:", self.data.shape[1])

        except FileNotFoundError:

            print("\nFile not found! Please check the file path.")

        except Exception as e:

            print("\nError while loading dataset:", e)

    # ==================================================
    # EXPLORE DATA
    # ==================================================

    def explore_data(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        while True:

            print("\n========== Explore Data of Sales ==========")
            print("1. Display first 5 rows")
            print("2. Display last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display shape")
            print("6. Display basic information")
            print("7. Display descriptive statistics")
            print("8. Back to Main Menu")

            try:

                choice = int(
                    input("Enter your choice: ")
                )

            except ValueError:

                print("\nPlease enter a valid number.")
                continue

            if choice == 1:

                print("\nFirst 5 rows:")
                print(self.data.head())

            elif choice == 2:

                print("\nLast 5 rows:")
                print(self.data.tail())

            elif choice == 3:

                print("\nColumn Names:")
                print(self.data.columns.tolist())

            elif choice == 4:

                print("\nData Types:")
                print(self.data.dtypes)

            elif choice == 5:

                print("\nDataset Shape:")
                print(self.data.shape)

            elif choice == 6:

                print("\nBasic Information:")
                self.data.info()

            elif choice == 7:

                print("\nDescriptive Statistics:")
                print(self.data.describe())

            elif choice == 8:

                break

            else:

                print("\nInvalid choice.")

    # ==================================================
    # CLEAN DATA
    # ==================================================

    def clean_data(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        print("\n========== Cleaning Sales Data ==========")

        print("\nMissing values before cleaning:")
        print(self.data.isnull().sum())

        # Fill numerical missing values

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        for column in numeric_columns:

            if self.data[column].isnull().any():

                self.data[column] = self.data[column].fillna(
                    self.data[column].mean()
                )

        # Fill categorical missing values

        categorical_columns = self.data.select_dtypes(
            include="object"
        ).columns

        for column in categorical_columns:

            if self.data[column].isnull().any():

                self.data[column] = self.data[column].fillna(
                    self.data[column].mode()[0]
                )

        # Convert date column

        if "Sale_Date" in self.data.columns:

            self.data["Sale_Date"] = pd.to_datetime(
                self.data["Sale_Date"],
                errors="coerce"
            )

        # Remove duplicate rows

        self.data.drop_duplicates(
            inplace=True
        )

        print("\nMissing values after cleaning:")
        print(self.data.isnull().sum())

        print("\nData cleaning completed successfully!")

    # ==================================================
    # NUMPY ARRAY OPERATIONS
    # ==================================================

    def numpy_array_operations(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns.tolist()

        if len(numeric_columns) == 0:

            print("\nNo numerical columns available.")
            return

        print("\n========== NumPy Array Operations ==========")

        print("\nNumerical Columns:")

        for i, column in enumerate(
            numeric_columns,
            1
        ):

            print(f"{i}. {column}")

        try:

            choice = int(
                input(
                    "\nSelect column number: "
                )
            )

        except ValueError:

            print("\nPlease enter a valid number.")
            return

        if choice < 1 or choice > len(numeric_columns):

            print("\nInvalid column choice.")
            return

        column = numeric_columns[
            choice - 1
        ]

        array = self.data[column].to_numpy()

        print(f"\nNumPy Array of {column}:")
        print(array)

        while True:

            print("\n========== NumPy Operations ==========")
            print("1. Display Index")
            print("2. Display Slicing")
            print("3. Display Array Shape")
            print("4. Display Array Data Type")
            print("5. Back to Main Menu")

            try:

                operation = int(
                    input("Enter your choice: ")
                )

            except ValueError:

                print("\nPlease enter a valid number.")
                continue

            if operation == 1:

                try:

                    index = int(
                        input("Enter index: ")
                    )

                    print(
                        "\nElement at index:",
                        array[index]
                    )

                except IndexError:

                    print("\nIndex out of range.")

                except ValueError:

                    print("\nEnter a valid index.")

            elif operation == 2:

                try:

                    start = int(
                        input("Enter starting index: ")
                    )

                    end = int(
                        input("Enter ending index: ")
                    )

                    print(
                        "\nSliced Array:"
                    )

                    print(
                        array[start:end]
                    )

                except ValueError:

                    print("\nEnter valid numbers.")

            elif operation == 3:

                print(
                    "\nArray Shape:",
                    array.shape
                )

            elif operation == 4:

                print(
                    "\nArray Data Type:",
                    array.dtype
                )

            elif operation == 5:

                break

            else:

                print("\nInvalid choice.")

    # ==================================================
    # MATHEMATICAL OPERATIONS
    # ==================================================

    def mathematical_operations(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns.tolist()

        print("\n========== Mathematical Operations ==========")

        for i, column in enumerate(
            numeric_columns,
            1
        ):

            print(f"{i}. {column}")

        if len(numeric_columns) < 2:

            print(
                "\nAt least two numerical columns are required."
            )

            return

        try:

            col1_choice = int(
                input(
                    "\nEnter first column number: "
                )
            )

            col2_choice = int(
                input(
                    "Enter second column number: "
                )
            )

        except ValueError:

            print("\nPlease enter valid numbers.")
            return

        if (
            col1_choice < 1
            or col1_choice > len(numeric_columns)
            or col2_choice < 1
            or col2_choice > len(numeric_columns)
        ):

            print("\nInvalid column choice.")
            return

        column1 = numeric_columns[
            col1_choice - 1
        ]

        column2 = numeric_columns[
            col2_choice - 1
        ]

        print(
            f"\nSelected: {column1} and {column2}"
        )

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Square Root")

        try:

            choice = int(
                input(
                    "Enter your choice: "
                )
            )

        except ValueError:

            print("\nInvalid choice.")
            return

        if choice == 1:

            result = (
                self.data[column1]
                + self.data[column2]
            )

            print("\nAddition:")
            print(result.head())

        elif choice == 2:

            result = (
                self.data[column1]
                - self.data[column2]
            )

            print("\nSubtraction:")
            print(result.head())

        elif choice == 3:

            result = (
                self.data[column1]
                * self.data[column2]
            )

            print("\nMultiplication:")
            print(result.head())

        elif choice == 4:

            result = (
                self.data[column1]
                / self.data[column2]
            )

            print("\nDivision:")
            print(result.head())

        elif choice == 5:

            result = np.square(
                self.data[column1]
            )

            print("\nSquare:")
            print(result.head())

        elif choice == 6:

            result = np.sqrt(
                self.data[column1]
            )

            print("\nSquare Root:")
            print(result.head())

        else:

            print("\nInvalid choice.")

    # ==================================================
    # COMBINE DATA
    # ==================================================

    def combine_data(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        print("\n========== Combine DataFrames ==========")

        file_path = input(
            "Enter path of second CSV file: "
        )

        try:

            other_dataframe = pd.read_csv(
                file_path
            )

            print(
                "\nSecond DataFrame loaded successfully!"
            )

            print(
                "Shape:",
                other_dataframe.shape
            )

            print("\n1. Concatenate using concat")
            print("2. Merge using merge")
            print("3. Join using join")
            print("4. Back")

            choice = int(
                input("Enter your choice: ")
            )

            if choice == 1:

                result = pd.concat(
                    [
                        self.data,
                        other_dataframe
                    ],
                    ignore_index=True
                )

                print("\nDataFrames combined using concat:")
                print(result.head())

                print(
                    "\nCombined Shape:",
                    result.shape
                )

                self.data = result

            elif choice == 2:

                print(
                    "\nCurrent DataFrame columns:"
                )

                print(
                    self.data.columns.tolist()
                )

                print(
                    "\nSecond DataFrame columns:"
                )

                print(
                    other_dataframe.columns.tolist()
                )

                column = input(
                    "\nEnter common column: "
                )

                if column not in self.data.columns:

                    print("\nColumn not found.")
                    return

                if column not in other_dataframe.columns:

                    print("\nColumn not found.")
                    return

                result = pd.merge(
                    self.data,
                    other_dataframe,
                    on=column,
                    how="inner"
                )

                print(
                    "\nMerged DataFrame:"
                )

                print(result.head())

                self.data = result

            elif choice == 3:

                result = self.data.join(
                    other_dataframe,
                    lsuffix="_left",
                    rsuffix="_right"
                )

                print(
                    "\nJoined DataFrame:"
                )

                print(result.head())

                self.data = result

            elif choice == 4:

                return

            else:

                print("\nInvalid choice.")

        except FileNotFoundError:

            print("\nFile not found.")

        except Exception as e:

            print(
                "\nError:",
                e
            )

    # ==================================================
    # SPLIT DATA
    # ==================================================

    def split_data(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        print("\n========== Split DataFrame ==========")

        print("1. Split by Region")
        print("2. Split by Product Category")
        print("3. Split by Sales Representative")
        print("4. Back")

        try:

            choice = int(
                input("Enter your choice: ")
            )

        except ValueError:

            print("\nInvalid choice.")
            return

        if choice == 1:

            column = "Region"

        elif choice == 2:

            column = "Product_Category"

        elif choice == 3:

            column = "Sales_Rep"

        elif choice == 4:

            return

        else:

            print("\nInvalid choice.")
            return

        if column not in self.data.columns:

            print(
                f"\nColumn '{column}' not found."
            )

            return

        print(
            f"\nSplitting by {column}..."
        )

        for value in self.data[column].dropna().unique():

            split_dataframe = self.data[
                self.data[column] == value
            ]

            print("\n------------------------------")
            print(f"{column}: {value}")
            print("------------------------------")

            print(
                "Number of rows:",
                split_dataframe.shape[0]
            )

            print(
                split_dataframe.head()
            )

        print(
            "\nDataFrame split successfully!"
        )

    # ==================================================
    # SEARCH, SORT, FILTER
    # ==================================================

    def search_sort_filter(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        while True:

            print(
                "\n========== Search, Sort, or Filter Data =========="
            )

            print("1. Search Data")
            print("2. Sort Data")
            print("3. Filter Data")
            print("4. Back")

            try:

                choice = int(
                    input("Enter your choice: ")
                )

            except ValueError:

                print("\nInvalid choice.")
                continue

            if choice == 1:

                print(
                    "\nAvailable Columns:"
                )

                print(
                    self.data.columns.tolist()
                )

                column = input(
                    "\nEnter column name: "
                )

                if column not in self.data.columns:

                    print("\nColumn not found.")
                    continue

                value = input(
                    "Enter search value: "
                )

                result = self.data[
                    self.data[column]
                    .astype(str)
                    .str.contains(
                        value,
                        case=False,
                        na=False
                    )
                ]

                print("\nSearch Result:")
                print(result)

            elif choice == 2:

                print(
                    "\nAvailable Columns:"
                )

                print(
                    self.data.columns.tolist()
                )

                column = input(
                    "\nEnter column name: "
                )

                if column not in self.data.columns:

                    print("\nColumn not found.")
                    continue

                print("\n1. Ascending")
                print("2. Descending")

                order = int(
                    input(
                        "Enter choice: "
                    )
                )

                if order == 1:

                    result = self.data.sort_values(
                        by=column
                    )

                elif order == 2:

                    result = self.data.sort_values(
                        by=column,
                        ascending=False
                    )

                else:

                    print("\nInvalid choice.")
                    continue

                print("\nSorted Data:")
                print(result.head())

            elif choice == 3:

                print(
                    "\nAvailable Columns:"
                )

                print(
                    self.data.columns.tolist()
                )

                column = input(
                    "\nEnter column name: "
                )

                if column not in self.data.columns:

                    print("\nColumn not found.")
                    continue

                value = input(
                    "Enter filter value: "
                )

                result = self.data[
                    self.data[column]
                    .astype(str)
                    .str.lower()
                    == value.lower()
                ]

                print("\nFiltered Data:")
                print(result)

            elif choice == 4:

                break

            else:

                print("\nInvalid choice.")

    # ==================================================
    # AGGREGATE FUNCTIONS
    # ==================================================

    def aggregate_functions(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns.tolist()

        print("\n========== Compute Aggregates ==========")

        for i, column in enumerate(
            numeric_columns,
            1
        ):

            print(
                f"{i}. {column}"
            )

        try:

            choice = int(
                input(
                    "\nSelect column: "
                )
            )

        except ValueError:

            print("\nInvalid choice.")
            return

        if choice < 1 or choice > len(numeric_columns):

            print("\nInvalid column.")
            return

        column = numeric_columns[
            choice - 1
        ]

        print(
            f"\nSelected Column: {column}"
        )

        print(
            "\nSum:",
            self.data[column].sum()
        )

        print(
            "Mean:",
            self.data[column].mean()
        )

        print(
            "Count:",
            self.data[column].count()
        )

        print(
            "Minimum:",
            self.data[column].min()
        )

        print(
            "Maximum:",
            self.data[column].max()
        )

        print(
            "Median:",
            self.data[column].median()
        )

    # ==================================================
    # STATISTICAL ANALYSIS
    # ==================================================

    def statistical_analysis(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        print(
            "\n========== Statistical Analysis =========="
        )

        numeric_data = self.data.select_dtypes(
            include=np.number
        )

        if numeric_data.empty:

            print(
                "\nNo numerical columns found."
            )

            return

        print("\nDescriptive Statistics:")

        print(
            numeric_data.describe()
        )

        print("\nMean:")

        print(
            numeric_data.mean()
        )

        print("\nStandard Deviation:")

        print(
            numeric_data.std()
        )

        print("\nVariance:")

        print(
            numeric_data.var()
        )

        print("\n25th Percentile:")

        print(
            numeric_data.quantile(0.25)
        )

        print("\n50th Percentile:")

        print(
            numeric_data.quantile(0.50)
        )

        print("\n75th Percentile:")

        print(
            numeric_data.quantile(0.75)
        )

        print("\nCorrelation Matrix:")

        print(
            numeric_data.corr()
        )

    # ==================================================
    # PIVOT TABLE
    # ==================================================

    def create_pivot_table(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        print(
            "\n========== Create Pivot Table =========="
        )

        print(
            "\nAvailable Columns:"
        )

        print(
            self.data.columns.tolist()
        )

        index_column = input(
            "\nEnter index column: "
        )

        value_column = input(
            "Enter value column: "
        )

        if index_column not in self.data.columns:

            print("\nIndex column not found.")
            return

        if value_column not in self.data.columns:

            print("\nValue column not found.")
            return

        pivot = pd.pivot_table(
            self.data,
            index=index_column,
            values=value_column,
            aggfunc="sum"
        )

        print(
            "\nPivot Table:"
        )

        print(pivot)

    # ==================================================
    # GROUPBY AND TRANSFORM
    # ==================================================

    def groupby_analysis(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        print(
            "\n========== GroupBy Analysis =========="
        )

        print(
            "\nAvailable Columns:"
        )

        print(
            self.data.columns.tolist()
        )

        group_column = input(
            "\nEnter grouping column: "
        )

        value_column = input(
            "Enter numerical column: "
        )

        if group_column not in self.data.columns:

            print("\nGrouping column not found.")
            return

        if value_column not in self.data.columns:

            print("\nValue column not found.")
            return

        result = self.data.groupby(
            group_column
        )[value_column].agg(
            ["sum", "mean", "count"]
        )

        print(
            "\nGroupBy Result:"
        )

        print(result)

        self.data[
            "Group_Mean"
        ] = self.data.groupby(
            group_column
        )[value_column].transform(
            "mean"
        )

        print(
            "\nData after transform():"
        )

        print(
            self.data[
                [
                    group_column,
                    value_column,
                    "Group_Mean"
                ]
            ].head()
        )

    # ==================================================
    # DATA VISUALIZATION
    # ==================================================

    def visualize_data(self):

        if self.data is None:

            print("\nPlease load the dataset first.")
            return

        while True:

            print(
                "\n========== Data Visualization =========="
            )

            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Subplots")
            print("8. Seaborn Heatmap")
            print("9. Seaborn Box Plot")
            print("10. Back to Main Menu")

            try:

                choice = int(
                    input(
                        "Enter your choice: "
                    )
                )

            except ValueError:

                print(
                    "\nPlease enter a valid number."
                )

                continue

            # --------------------------------
            # BAR PLOT
            # --------------------------------

            if choice == 1:

                column = input(
                    "\nEnter category column: "
                )

                value = input(
                    "Enter numerical column: "
                )

                if (
                    column not in self.data.columns
                    or value not in self.data.columns
                ):

                    print(
                        "\nInvalid column."
                    )

                    continue

                grouped = self.data.groupby(
                    column
                )[value].sum()

                plt.figure()

                grouped.plot(
                    kind="bar"
                )

                plt.title(
                    f"{value} by {column}"
                )

                plt.xlabel(column)

                plt.ylabel(value)

                plt.tight_layout()

                plt.show()

            # --------------------------------
            # LINE PLOT
            # --------------------------------

            elif choice == 2:

                x = input(
                    "\nEnter X-axis column: "
                )

                y = input(
                    "Enter Y-axis column: "
                )

                if (
                    x not in self.data.columns
                    or y not in self.data.columns
                ):

                    print(
                        "\nInvalid column."
                    )

                    continue

                plt.figure()

                plt.plot(
                    self.data[x],
                    self.data[y],
                    marker="o"
                )

                plt.title(
                    f"{y} vs {x}"
                )

                plt.xlabel(x)

                plt.ylabel(y)

                plt.xticks(
                    rotation=45
                )

                plt.tight_layout()

                plt.show()

            # --------------------------------
            # SCATTER PLOT
            # --------------------------------

            elif choice == 3:

                x = input(
                    "\nEnter X-axis numerical column: "
                )

                y = input(
                    "Enter Y-axis numerical column: "
                )

                if (
                    x not in self.data.columns
                    or y not in self.data.columns
                ):

                    print(
                        "\nInvalid column."
                    )

                    continue

                plt.figure()

                plt.scatter(
                    self.data[x],
                    self.data[y]
                )

                plt.title(
                    f"{y} vs {x}"
                )

                plt.xlabel(x)

                plt.ylabel(y)

                plt.tight_layout()

                plt.show()

            # --------------------------------
            # PIE CHART
            # --------------------------------

            elif choice == 4:

                column = input(
                    "\nEnter category column: "
                )

                if column not in self.data.columns:

                    print(
                        "\nColumn not found."
                    )

                    continue

                values = self.data[
                    column
                ].value_counts()

                plt.figure()

                plt.pie(
                    values,
                    labels=values.index,
                    autopct="%1.1f%%"
                )

                plt.title(
                    f"Distribution of {column}"
                )

                plt.show()

            # --------------------------------
            # HISTOGRAM
            # --------------------------------

            elif choice == 5:

                column = input(
                    "\nEnter numerical column: "
                )

                if column not in self.data.columns:

                    print(
                        "\nColumn not found."
                    )

                    continue

                plt.figure()

                plt.hist(
                    self.data[column].dropna(),
                    bins=10
                )

                plt.title(
                    f"Distribution of {column}"
                )

                plt.xlabel(column)

                plt.ylabel("Frequency")

                plt.tight_layout()

                plt.show()

            # --------------------------------
            # STACK PLOT
            # --------------------------------

            elif choice == 6:

                numeric_columns = self.data.select_dtypes(
                    include=np.number
                ).columns.tolist()

                if len(numeric_columns) < 2:

                    print(
                        "\nAt least two numerical columns are required."
                    )

                    continue

                print(
                    "\nNumerical Columns:"
                )

                for i, column in enumerate(
                    numeric_columns,
                    1
                ):

                    print(
                        f"{i}. {column}"
                    )

                try:

                    first = int(
                        input(
                            "\nSelect first column: "
                        )
                    )

                    second = int(
                        input(
                            "Select second column: "
                        )
                    )

                except ValueError:

                    print(
                        "\nInvalid choice."
                    )

                    continue

                data1 = self.data[
                    numeric_columns[first - 1]
                ]

                data2 = self.data[
                    numeric_columns[second - 1]
                ]

                x = np.arange(
                    len(self.data)
                )

                plt.figure()

                plt.stackplot(
                    x,
                    data1,
                    data2,
                    labels=[
                        numeric_columns[first - 1],
                        numeric_columns[second - 1]
                    ]
                )

                plt.title(
                    "Stack Plot"
                )

                plt.legend()

                plt.tight_layout()

                plt.show()

            # --------------------------------
            # SUBPLOTS
            # --------------------------------

            elif choice == 7:

                numeric_columns = self.data.select_dtypes(
                    include=np.number
                ).columns.tolist()

                if len(numeric_columns) < 2:

                    print(
                        "\nAt least two numerical columns are required."
                    )

                    continue

                first = numeric_columns[0]

                second = numeric_columns[1]

                fig, axes = plt.subplots(
                    1,
                    2,
                    figsize=(12, 5)
                )

                axes[0].hist(
                    self.data[first].dropna(),
                    bins=10
                )

                axes[0].set_title(
                    f"{first} Distribution"
                )

                axes[1].hist(
                    self.data[second].dropna(),
                    bins=10
                )

                axes[1].set_title(
                    f"{second} Distribution"
                )

                plt.tight_layout()

                plt.show()

            # --------------------------------
            # HEATMAP
            # --------------------------------

            elif choice == 8:

                numeric_data = self.data.select_dtypes(
                    include=np.number
                )

                plt.figure(
                    figsize=(10, 6)
                )

                sns.heatmap(
                    numeric_data.corr(),
                    annot=True,
                    cmap="coolwarm"
                )

                plt.title(
                    "Correlation Heatmap"
                )

                plt.tight_layout()

                plt.show()

            # --------------------------------
            # BOX PLOT
            # --------------------------------

            elif choice == 9:

                column = input(
                    "\nEnter numerical column: "
                )

                if column not in self.data.columns:

                    print(
                        "\nColumn not found."
                    )

                    continue

                plt.figure()

                sns.boxplot(
                    x=self.data[column]
                )

                plt.title(
                    f"Box Plot of {column}"
                )

                plt.tight_layout()

                plt.show()

            elif choice == 10:

                break

            else:

                print(
                    "\nInvalid choice."
                )

    # ==================================================
    # SAVE DATA
    # ==================================================

    def save_data(self):

        if self.data is None:

            print(
                "\nPlease load the dataset first."
            )

            return

        file_path = input(
            "\nEnter file name to save CSV: "
        )

        try:

            self.data.to_csv(
                file_path,
                index=False
            )

            print(
                "\nData saved successfully!"
            )

        except Exception as e:

            print(
                "\nError while saving:",
                e
            )


# ==================================================
# MAIN PROGRAM
# ==================================================

print(
    "Welcome to the Pandas Analyzer & Data Visualization!"
)

print(
    "======================================================"
)

analyzer = SalesDataAnalyzer()


while True:

    print(
        "\n========== Main Menu =========="
    )

    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Clean Data")
    print("4. NumPy Array Operations")
    print("5. Mathematical Operations")
    print("6. Combine Data")
    print("7. Split Data")
    print("8. Search, Sort, or Filter Data")
    print("9. Compute Aggregates")
    print("10. Statistical Analysis")
    print("11. Create Pivot Table")
    print("12. GroupBy and Transform")
    print("13. Data Visualization")
    print("14. Save Data")
    print("15. Exit")

    try:

        choice = int(
            input(
                "\nEnter your choice: "
            )
        )

    except ValueError:

        print(
            "\nPlease enter a valid number."
        )

        continue

    # --------------------------------
    # 1. LOAD
    # --------------------------------

    if choice == 1:

        analyzer.load_data()

    # --------------------------------
    # 2. EXPLORE
    # --------------------------------

    elif choice == 2:

        analyzer.explore_data()

    # --------------------------------
    # 3. CLEAN
    # --------------------------------

    elif choice == 3:

        analyzer.clean_data()

    # --------------------------------
    # 4. NUMPY
    # --------------------------------

    elif choice == 4:

        analyzer.numpy_array_operations()

    # --------------------------------
    # 5. MATHEMATICAL
    # --------------------------------

    elif choice == 5:

        analyzer.mathematical_operations()

    # --------------------------------
    # 6. COMBINE
    # --------------------------------

    elif choice == 6:

        analyzer.combine_data()

    # --------------------------------
    # 7. SPLIT
    # --------------------------------

    elif choice == 7:

        analyzer.split_data()

    # --------------------------------
    # 8. SEARCH SORT FILTER
    # --------------------------------

    elif choice == 8:

        analyzer.search_sort_filter()

    # --------------------------------
    # 9. AGGREGATE
    # --------------------------------

    elif choice == 9:

        analyzer.aggregate_functions()

    # --------------------------------
    # 10. STATISTICS
    # --------------------------------

    elif choice == 10:

        analyzer.statistical_analysis()

    # --------------------------------
    # 11. PIVOT TABLE
    # --------------------------------

    elif choice == 11:

        analyzer.create_pivot_table()

    # --------------------------------
    # 12. GROUPBY
    # --------------------------------

    elif choice == 12:

        analyzer.groupby_analysis()

    # --------------------------------
    # 13. VISUALIZATION
    # --------------------------------

    elif choice == 13:

        analyzer.visualize_data()

    # --------------------------------
    # 14. SAVE
    # --------------------------------

    elif choice == 14:

        analyzer.save_data()

    # --------------------------------
    # 15. EXIT
    # --------------------------------

    elif choice == 15:

        print(
            "\nThank you for using Pandas Analyzer!"
        )

        break

    else:

        print(
            "\nInvalid choice! "
            "Please select 1 to 15."
        )
