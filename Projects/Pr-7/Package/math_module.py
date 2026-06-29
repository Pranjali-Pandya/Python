def math_module():

    import math

    print("\n**********************Math Module*******************************")

    while(True):
        print("1. Trigonometric Calculations")
        print("2. To find factorial")
        print("3. Logaritmns calculations")
        print("4. Calculate Compound Interest")
        print("5. Area of Geometric Shapes")
        print("6. Exit")

        c = int(input("Enter your choice "))

        if c == 1:
            print("\n=====================Trigonometric Calculations============================")
            print("1. Sine (degree -> sin)")
            print("2. Cosine (degree -> cos)")
            print("3. Tangent(degree -> tan)")
            print("4. Inverse sine (value -> angle )")
            print("5. Inverse cosine (value -> angle )")
            print("6. Inverse tangent (value -> angle )")
            print("7. Exit ")

            choice = int(input("Enter your choice "))

            if choice == 1:
                degree = int(input("Enter the degree"))
                print("Degree into sin ", math.sin(math.radians(degree)))

            elif choice == 2:
                degree = int(input("Enter the degree"))
                print("Degree into cos ", math.cos(math.radians(degree)))

            elif choice == 3:
                degree = int(input("Enter the degree"))
                print("Degree into tan ", math.tan(math.radians(degree)))

            elif choice == 4:
                value = float(input("Enter the number between -1 and 1: "))
                if value < -1 or value > 1:
                    print("Invalid Input")
                else:
                    print("Inverse sine ", math.degrees(math.asin(value)))

            elif choice == 5:
                value = float(input("Enter the number between -1 and 1: "))
                if value < -1 or value > 1:
                    print("Invalid Input")
                else:
                    print("Inverse cos ", math.degrees(math.acos(value)))

            elif choice == 6:
                value = float(input("Enter the number "))
                print("Inverse tan ", math.degrees(math.atan(value)))

            elif choice == 7:
                print("\n Thankyou for using Trigonometric functions\n")
                break

            else:
                print("Invalid Number")

        elif c == 2:
            number = int(input("Enter the number: "))
            print(f"Factorial of {number}", math.factorial(number))

        elif c == 3:
            print("1. Natural Log(ln)")
            print("2. Log Base 10")
            print("3. Log with custom base")
            print("4. Exit")

            choice = int(input("Enter your choice "))

            if choice == 1:
                number = float(input("Enter the number you want to find natural log : "))
                if number > 0:
                    print(math.log(number))
                else:
                    print("Number must be greater then 0 ")

            elif choice == 2:
                number = float(input("Enter the number you want to find log base10 : "))
                if number > 0:
                    print(math.log10(number))
                else:
                    print("Number must be greater then 0 ")

            elif choice == 3:
                number = float(input("Enter the number you want to find natural log : "))
                base = float(input("Enter the base : "))

                if number > 0 and base != 1 and base > 0:
                    print(math.log(number, base))
                else:
                    print("Invalid Input")

            else:
                print("Invalid Input")

        elif c == 4:
            
                principle = float(input("Enter the principle amount: "))
                rate = float(input("Enter the rate of interest: "))
                time = float(input("Enter the input in years: "))
                n = int(input("Number of times interest is compounded per year: "))
                if principle > 0 and rate >= 0 and time > 0 and n > 0:
                    # Compound Interest = A - P
                    amount = principle * (1 + rate / (100 * n)) ** (n * time)
                    compound_interest = amount - principle
                    print("The Compound Interest ", compound_interest)

                else:
                    print("Enter valid Input")

        elif c == 5:
            print("\nArea of Circle")
            radius = int(input("Enter the radius of the circle: "))
            area = math.pi * radius * radius
            print("The area of circle: ", area)

        elif c == 6:
            print("\n*******************Thankyou for using Math Module*********************\n")
            break

        else:
            print("Invalid choice")
if __name__ == "__main__":
    print("Inside package running")
    math_module()
