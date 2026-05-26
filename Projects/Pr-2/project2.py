print("Welcome to the Pattern Generator and Nimber Analyzer \n \n")

o = -1

while o!=0:
    print("Select an option from below")
    print("1. To Generate a Pattern")
    print("2. To analyze a Range of Numbers")
    print("3. To Exit")
    o = int(input("Enter choice: "))

    match o:
        case 1:
            n = -1
            while n!=0:  
                print("Select an option from below")
                print("1. Right-angled triangle")
                print("2. Inverted right-angled triangle")
                print("3. Same number triangle")
                print("4. Reverse Incrementing Number Triangle Pattern")
                print("5. To exit")
                n = int(input("Enter choice: "))
                match n:
                    case 1:
                        r = int(input("Enter the number of rows for  pattern"))
                        print("Right angled triangle pattern")
                        for i in range(1,r+1):
                            for j in range(1,i+1):
                                print(j, end="")
                            print()
                        
                    case 2:
                        r = int(input("Enter the number of rows for  pattern"))
                        print("Inverted Right angeled triangle pattern")
                        for i in range(r,0,-1):
                            for j in range(1,i+1):
                                print(j, end = "")
                            print()
    
                    case 3:
                        r = int(input("Enter the number of rows for  pattern"))
                        print("Same Number Triangle")
                        for i in range(1,r+1):
                           print(str(i) *i )
                    case 4:
                        r = int(input("Enter the number of rows for  pattern"))
                        print("Reverse incrementing number triangle")
                        
                        for i in range(r+1,0,-1):
                           for j in range(r+1,i-1,-1):
                                print(j, end="")
                        print()
                    case 5:
                        print("End of patter")
                        break
                    case _:
                        print("Invalid choice")
                                 
        case 2:
            a = int(input("Enter the start of range "))
            b = int(input("Enter the end of range "))        
            sum = 0
            for i in range(a,b+1):
                if(i%2==0):
                    print(f"The number {i} is even ")
                else:
                    print(f"The number {i} is odd ")
                sum = sum + i
            print(f"The sum of all numbers between {a} & {b} is ",sum )
                                    
        case 3:
            print("Thankyou for using Pattern Generator and Nimber Analyzer")
            break
            
        case _:
            print("Invalid choice")
