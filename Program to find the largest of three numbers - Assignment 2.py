# Program to find the largest of three numbers

# Take three integer inputs from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Compare the numbers
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

# Display
print(f"The largest number among {num1}, {num2}, {num3} is {largest}.")


