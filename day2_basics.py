# Day 2 - Student Grading System with Input Validation

try:
    marks = float(input("Enter your marks (0 - 100): "))

    # --- Input Validation using logical 'or' ---
    if marks < 0 or marks > 100:
        print("❌ Invalid marks! Score must be between 0 and 100.")
    else:
        # --- Grade Assignment using if / elif / else ---
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        # --- Pass / Fail Check using comparison + logical 'and' ---
        if marks >= 50 and marks <= 100:
            status = "Passed ✅"
        else:
            status = "Failed ❌"

        # --- Display Result ---
        print("\n----- Result -----")
        print(f"Marks : {marks}")
        print(f"Grade : {grade}")
        print(f"Status: {status}")

except ValueError:
    # Catches non-numeric inputs like "abc", "#$%", "" etc.
    print("❌ Invalid input! Please enter a numeric value.")