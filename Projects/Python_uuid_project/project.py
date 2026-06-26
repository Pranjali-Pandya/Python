import uuid

order = {}

print("\n******************** E-Commerce Order System using Python UUID Module ********************\n")

while True:

    print("\n1. To Place Order")
    print("2. To View Orders")
    print("3. To Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:

        prod_name = input("\nEnter the product name: ")

        order[prod_name] = uuid.uuid4()

        print("\nOrder Placed Successfully!\n")

        print("Product Name :", prod_name)
        print("Order ID     :", order[prod_name])

    elif ch == 2:

        if not order:

            print("\nNo orders have been placed yet.\n")

        else:

            print("\n========================= All Orders =========================\n")

            k = 0

            for i, j in order.items():

                k += 1

                print(f"Order {k}")
                print("-------------------------------------------------------")
                print("Product  :", i)
                print("Order ID :", j)
                print()

    elif ch == 3:

        print("\nThank you for using E-Commerce Order System")
        break

    else:

        print("Invalid choice")
