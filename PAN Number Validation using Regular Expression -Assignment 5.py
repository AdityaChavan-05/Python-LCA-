# PAN Number Validation using Regular Expression

import re

def validate_pan(pan):
    # Regex pattern: 5 uppercase letters, 4 digits, 1 uppercase letter
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    
    if re.match(pattern, pan):
        return "Valid PAN Number"
    else:
        return "Invalid PAN Number"

# Accept PAN number from user
pan_number = input("Enter PAN Number: ")

# Validate and display result
print(validate_pan(pan_number))
