numbers = []
for number in range(1, 5 + 1):
    new_number = float(input("Number: "))
    numbers.append(new_number)
average = sum(numbers) / len(numbers)

print("The first number is {}".format(int(numbers[0])))
print("The last number is {}".format(int(numbers[4])))
print("The smallest number is {}".format(int(min(numbers))))
print("The largest number is {}".format(int(max(numbers))))
print("The average of the numbers is {}".format(average))
