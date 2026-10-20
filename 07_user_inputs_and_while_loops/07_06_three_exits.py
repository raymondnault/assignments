'''

Raymond Nault
Chapter 7: User Inputs and While Loops

'''

# this code will demonstrate three different ways to exit a while loop

# exit with condition
count = 0
while count < 5:
    print(count)
    count += 1
print("Exited loop with condition")

# exit with break
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
    print('Exited loop with break')

# exit with return (using a function)
def exit_with_return():
    count = 0
    while True:
        print(count)
        count += 1
        if count >= 5:
            return
        print('Exited loop with return')

exit_with_return()
print("Exited loop with return")