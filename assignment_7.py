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

    if len(parts) == 5:
        code = parts[0].strip().upper()
        
        # .title() capitalizes the first letter of every word
        title = parts[1].strip().title() 
        
        days = parts[2].strip() # We will handle days in Step 3
        time = parts[3].strip() # We will handle time in Step 4
        
        # .title() ensures rooms like "ncat 101" become "Ncat 101"
        room = parts[4].strip().title() 

        # Store the cleaned data
        all_courses.append([code, title, days, time, room])


# ============================================================
# Step 3: Day Code Expansion
# ============================================================
        
# Mapping dictionaries for expansion
full_map = {"M": "Monday", "T": "Tuesday", "W": "Wednesday", "R": "Thursday", "F": "Friday"}
short_map = {"M": "Mon", "T": "Tue", "W": "Wed", "R": "Thu", "F": "Fri"}
        
# Lists to hold the expanded strings
expanded_full = []
expanded_short = []
        
# We loop through each character in the days string.
# .upper() ensures that 'm' or 'M' both work correctly.
for char in days.upper():
  if char in full_map:
    expanded_full.append(full_map[char])
    expanded_short.append(short_map[char])   
# .join() combines the list items into a single string separated by "/"
full_days = "/".join(expanded_full)
short_days = "/".join(expanded_short)

# ============================================================
# Step 4: Time Standardization
# ============================================================
        
# 1. Remove all spaces and convert to lowercase to make it predictable
clean_time = time.replace(" ", "").lower()
        
# 2. Separate the "am/pm" from the numbers. 
# We replace "am" with " AM" (with a space) and "pm" with " PM".
clean_time = clean_time.replace("am", " AM").replace("pm", " PM")
        
# 3. Final cleanup: ensure the AM/PM is uppercase
time = clean_time.upper()

# IMPORTANT: Now that all fields are clean, we store them together.
# We store both full_days and short_days for the different output sections.
all_courses.append({
  "code": code,
  "title": title,
  "full_days": full_days,
  "short_days": short_days,
  "time": time,
  "room": room,
  "raw_days": days.upper() # Keep raw days for conflict checking in Step 5
})

# ============================================================
# Step 5: Conflict Detection
# ============================================================


# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
