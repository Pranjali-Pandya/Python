print("Welocome to Interactive personal Data Collector")

name = input("Enter your name")
age = int(input("Enter your age"))
height = float(input("Enter yoyr height"))
num = int(input("Enter your favorite number"))


print("Thankyou! Here is the information we collected")
print("Name",name, "(Type:", type(name) , ", Memory Address : ",id(name),")")

print("Age",age, "(Type:", type(age) , ", Memory Address : ",id(age),")")

print("Height",height, "(Type:", type(height) , ", Memory Address : ",id(height),")")

print("Favorite Number",num, "(Type:", type(num) , ", Memory Address : ",id(num),")")

i=2026-age
print("Your Birth year is approximately ",i," f(based on your age of {age} ")

print("Thankyou! for using Personal Data Collector")