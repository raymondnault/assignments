'''

Raymond Nault
Chapter 3: Introducing Lists

'''



guest_list = ["Kendrick Lamar", "Christopher Nolan", "Tom Cruise", "Jalen Brunson"]

print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"Dear {guest_list[3]}, you are invited to dinner.")

print("\nUnfortunately, Tom Cruise can't make it to the dinner.")
guest_list[2] = "Leonardo DiCaprio"

print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"Dear {guest_list[3]}, you are invited to dinner.")