'''

Raymond Nault
Chapter 5: If Statements

'''

# series of statements to determine the stage of life based on age

age = 21
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")