# Student Data Management using Python Collections

# Each student record will be stored as a tuple: (Roll Number, Name, Branch, Marks)
# Dictionary will use Roll Number as the key and tuple as the value
students = {
    101: ("101", "Alice", "CSE", [85, 90, 88]),
    102: ("102", "Bob", "ECE", [78, 82, 80]),
    103: ("103", "Charlie", "ME", [92, 88, 95])
}

def display_students():
    print("\nFinal Student Records:")
    for roll, details in students.items():
        print(f"Roll No: {details[0]}, Name: {details[1]}, Branch: {details[2]}, Marks: {details[3]}")

# 1. Add a new student record
print("\nAdding a new student...")
students[104] = ("104", "David", "CIVIL", [70, 75, 72])

# 2. Delete an existing student record
print("\nDeleting student with Roll No 102...")
if 102 in students:
    del students[102]

# 3. Update the details of a student
print("\nUpdating student with Roll No 103...")
if 103 in students:
    # Convert tuple to list for modification
    roll, name, branch, marks = students[103]
    # Update branch and marks
    branch = "AERO"
    marks.append(97)  # Adding a new mark
    # Convert back to tuple and update the dictionary
    students[103] = (roll, name, branch, marks)
    
