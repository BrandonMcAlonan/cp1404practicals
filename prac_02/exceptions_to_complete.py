finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a valid number: "))
        finished = True
    except ValueError:
        print("Enter a valid number.")
print("Valid result is:", result)
