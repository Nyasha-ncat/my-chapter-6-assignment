"""
COMP 163 - Introduction to Programming
Assignment: Chapter 7 - Course Schedule Formatter
Name: [Nyasha Chimombe]
GitHub Username: [Nyasha-Ncat]
Date: [2/27/2026]
Description: [This program parses messy course registration data, cleans it using 
             string methods, detects scheduling conflicts, and prints a formatted schedule.]
AI Usage: [Describe any AI assistance OR write "None"]
"""

# ============================================================
# Step 1: Input Parsing & Course Code Formatting
# ============================================================

# List to store each course's data as a dictionary or sub-list
all_courses = []

print("Enter course data (format: code|title|days|time|room):")

while True:
    user_input = input().strip()
    
    # Check for exit condition
    if user_input.upper() == "DONE":
        break
    
    # Split the input into 5 parts based on the pipe character
    # Using .strip() on each part to remove accidental extra spaces
    parts = user_input.split('|')
    
    # Ensure the line has exactly 5 parts before processing
    if len(parts) == 5:
        code = parts[0].strip().upper()  # Standardize code to uppercase
        title = parts[1].strip()
        days = parts[2].strip()
        time = parts[3].strip()
        room = parts[4].strip()
        
        # Store data in a list to use in later steps
        all_courses.append([code, title, days, time, room])
    else:
        print("Invalid format. Please use: code|title|days|time|room")

# Verification print for Step 1 (You can remove this after testing)
for course in all_courses:
    print(f"Parsed Code: {course[0]}")


# ============================================================
# Step 2: Title and Room Formatting
# ============================================================


# ============================================================
# Step 3: Day Code Expansion
# ============================================================


# ============================================================
# Step 4: Time Standardization
# ============================================================


# ============================================================
# Step 5: Conflict Detection
# ============================================================


# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
