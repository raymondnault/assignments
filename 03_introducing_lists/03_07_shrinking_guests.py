'''

Raymond Nault
Chapter 3: Introducing Lists

'''



guest_list = ["Kendrick Lamar", "Christopher Nolan", "Leonardo DiCaprio", "Jalen Brunson", "Beyoncé", "Jay Z", "Oprah Winfrey"]
print("\nUnfortunately, we can only invite two people to dinner.")
pop_guest = guest_list.pop()
print(f"Sorry {pop_guest}, we can't invite you to dinner.")
pop_guest = guest_list.pop()
print(f"Sorry {pop_guest}, we can't invite you to dinner.")
pop_guest = guest_list.pop()
print(f"Sorry {pop_guest}, we can't invite you to dinner.")
pop_guest = guest_list.pop()
print(f"Sorry {pop_guest}, we can't invite you to dinner.")
pop_guest = guest_list.pop()
print(f"Sorry {pop_guest}, we can't invite you to dinner.")

print(f"Dear {guest_list[0]}, you are still invited to dinner.")
print(f"Dear {guest_list[1]}, you are still invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)