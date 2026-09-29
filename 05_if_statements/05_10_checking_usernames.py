'''

Raymond Nault
Chapter 5: If Statements

'''

# this program will check if a username has already been used

current_users = ['admin', 'ray', 'john', 'bob', 'alice']
new_users = ['admin', 'ray', 'mike', 'susan', 'alice']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, the username '{}' is already taken. Please choose a different username.".format(new_user))
    else:
        print("The username '{}' is available.".format(new_user))