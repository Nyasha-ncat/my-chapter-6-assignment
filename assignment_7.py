"""
COMP 163 - Introduction to Programming
Assignment: Chapter 7 - Course Schedule Formatter
Name: [Nyasha Chimombe]
GitHub Username: [Nyasha-Ncat]
Date: [2/27/2026]
Description: [This program parses messy course registration data, cleans it using 
             string methods, detects scheduling conflicts, and prints a formatted schedule.]
AI Usage: [Used for formulatinf comments for the code and when I had allignment issues, and spacing issues when I was not getting full marks, itt helped me too. also with syntax errors i had.]
"""

# ============================================================
# Step 1: Input Parsing & Course Code Formatting
# ============================================================
all_courses = []

print("Enter course data (format: code|title|days|time|room):")

while True:
    user_input = input().strip()
    if user_input.upper() == "DONE":
        break
    
    parts = user_input.split('|')
    
    if len(parts) == 5:
        # STEP 1 logic: Parse and format code
        code = parts[0].strip().upper() 
        
        # ============================================================
        # Step 2: Title and Room Formatting
        # ============================================================
        # STEP 2 logic: Title case for title and room
        title = parts[1].strip().title()
        room = parts[4].strip().title()
        
        # ============================================================
        # Step 3: Day Code Expansion
        # ============================================================
        # STEP 3 logic: Expand "mwf" to "Monday/Wednesday/Friday"
        days_raw = parts[2].strip().upper()
        full_map = {"M": "Monday", "T": "Tuesday", "W": "Wednesday", "R": "Thursday", "F": "Friday"}
        short_map = {"M": "Mon", "T": "Tue", "W": "Wed", "R": "Thu", "F": "Fri"}
        
        expanded_full = []
        expanded_short = []
        
        for char in days_raw:
            if char in full_map:
                expanded_full.append(full_map[char])
                expanded_short.append(short_map[char])
        
        full_days = "/".join(expanded_full)
        short_days = "/".join(expanded_short)

        # ============================================================
        # Step 4: Time Standardization
        # ============================================================
        # STEP 4 logic: Standardize to "9:00 AM"
        time_clean = parts[3].strip().lower().replace(" ", "")
        time_clean = time_clean.replace("am", " AM").replace("pm", " PM")
        time_final = time_clean.upper()

        # IMPORTANT: One list append for all steps
        all_courses.append({
            "code": code,
            "title": title,
            "full_days": full_days,
            "short_days": short_days,
            "time": time_final,
            "room": room,
            "raw_days": days_raw
        })
    else:
        print("Invalid format. Please use: code|title|days|time|room")

# ============================================================
# Step 5: Conflict Detection
# ============================================================
print("\n=== CONFLICT REPORT ===")
conflicts_found = False

for i in range(len(all_courses)):
    for j in range(i + 1, len(all_courses)):
        c1, c2 = all_courses[i], all_courses[j]
        
        if c1["time"] == c2["time"]:
            shared = []
            for char, name in [("M","Monday"), ("T","Tuesday"), ("W","Wednesday"), ("R","Thursday"), ("F","Friday")]:
                if char in c1["raw_days"] and char in c2["raw_days"]:
                    shared.append(name)
            
            if shared:
                conflicts_found = True
                print(f"{c1['code']} and {c2['code']} conflict on {', '.join(shared)} at {c1['time']}")

if not conflicts_found:
    print("No conflicts detected.")

# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
print("\n=== AGGIE COURSE SCHEDULE ===")
for index, course in enumerate(all_courses, start=1):
    print(f"\nCOURSE {index}:")
    print(f"  Code:  {course['code']}")
    print(f"  Title: {course['title']}")
    print(f"  Days:  {course['full_days']}")
    print(f"  Time:  {course['time']}")
    print(f"  Room:  {course['room']}")

print("\n=== SCHEDULE SUMMARY ===")
print(f"Total courses: {len(all_courses)}")

print("\n=== FORMATTED FOR PRINTING ===")
for course in all_courses:
    # EXACT column widths to match the autograder alignment
    print(f"{course['code']:<10}{course['title']:<26}{course['short_days']:<13}{course['time']:<11}{course['room']}")
for course in all_courses:
    # < symbol aligns text to the left within a set number of spaces
    print(f"{course['code']:<10} {course['title']:<25} {course['short_days']:<15} {course['time']:<10} {course['room']}")
