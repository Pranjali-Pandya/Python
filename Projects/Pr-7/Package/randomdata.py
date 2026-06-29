def random_module():

    import random
    print("\n**********************Random Module*******************************\n")
    while(True):
        print("1. To Generate a Random Number")
        print("2. To Generate a Random List")
        print("3. To Generate a Random Password")
        print("4. Exit")

        c = int(input("Enter your choice "))

        if c==1:
            print("1. To Generate Random Float Number")
            print("2. To Generate Random Integer Number between range 1 to 50")
            print("3. To Generate Random Odd Number between range 1 to 50")
            print("4. To Generate Random Float Number between range 1 to 10")
            ch = int(input("Enter your choice: "))

            if ch==1:
                print("Random Number ", random.random())
            elif ch==2:
                print("Random Number ", random.randint(1,50))
            elif ch==3:
                print("Random Odd Number ", random.randrange(1,50,2))
            elif ch==4:
                print("Random Odd Number ", random.uniform(1,10))
            else:
                print("Invalid choice")

        elif c==2:
            n = int(input("How much long List you want to make ?"))
            newlist = []

            for i in range(n):
                a = random.random()
                newlist.append(a)

            print("Your List is ", newlist)

        elif c==3:
            list_of_string = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxys','123456789','@#$%&!*']
            joined_string = "".join(list_of_string)
            password = ''
            print(joined_string)

            for i in range(6):
                password += random.choice(joined_string)

            print("Your password is ", password)

        elif c==4:
            print("\n*********************Thankyou for using Random Module***********************")
            break
        
        else:
            print("Invalid Option")
            
if __name__ == "__main__":
    print("Inside package running")
    random_module()
