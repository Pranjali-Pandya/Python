print("\n================================================")
print("Welcome To Multi-Utility Tool")
print("==================================================")
from Datetime_package.date_time_utils import date_timefunction
from Datetime_package.mathmodule import math_module
from Datetime_package.randomdata import random_module
from Datetime_package.uuid_module import uuid_function
from Datetime_package.file_module import file_module
from Datetime_package.explore_module_attributes import explore_module_attributes
while(True):
    print("\nChoose an option")
    print("1. Datetime and Time operations")
    print("2. Mathematical operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers(UUID)")
    print("5. File Operations ")
    print("6. Explore Module Attributes(dir()) ")
    print("7. Exit")
    print("==================================================")
    ch = int(input("Enter your choice: "))
    
    if ch ==1:
        date_timefunction()
        
    elif ch ==2:
        math_module()
    elif ch ==3:
        random_module()
          
    elif ch ==4:
        uuid_function()  
    elif ch ==5:
        file_module()
    elif ch ==6:
        explore_module_attributes()
    elif ch==7:
        print("\n--------------------------Thankyou for using Multi- Utility Tool----------------------")
        break
    else:
        print("Wrong choice")
        
    
    
    
