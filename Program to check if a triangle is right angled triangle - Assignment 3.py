# Program to check if a triangle is right-angled

def is_right_triangle(a, b, c):
    # Sort the sides so that the largest side is last
    sides = sorted([a, b, c])
    # Check Pythagoras theorem: hypotenuse^2 = sum of squares of other two sides
    return sides[2]**2 == sides[0]**2 + sides[1]**2

# Accept inputs from the user
side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))

# Check and display result
if is_right_triangle(side1, side2, side3):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is NOT a right-angled triangle.")
