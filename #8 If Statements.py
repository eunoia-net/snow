# if statement = a block of code that will execute if its condition is true
 
age = int(input("How old are you? : "))

#Order of If statements does matter 
#If you need to assign an equal if state do double equal sign 

if age == 100:
    print("You are a century old!")
elif age>= 18:
    print("You are an adult!")

elif age < 0:
     print("You haven't been born yet!")
       
else: 
    print("You are a child!")
