"""Student Result Checker"""


def safe_input(prompt, default=""):
    """Read input, but use a default when the user provides no input."""
    try:
        value = input(prompt).strip()
    except EOFError:
        print("No input provided. Using the default value.")
        return default
    return value if value else default


def get_student_details():
    """Collect basic student information from the user."""
    name = safe_input("Enter student name: ", "Asha")
    marks = float(safe_input("Enter marks (0-100): ", "75"))
    age = int(safe_input("Enter age: ", "20"))
    attendance = safe_input("Enter attendance percentage: ", "92")

    return name, marks, age, attendance


def calculate_grade(marks):
    """Return a grade based on marks."""
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"


def determine_pass_fail(marks):
    """Return pass or fail using a ternary-style expression."""
    return "PASS" if marks >= 40 else "FAIL"


def scholarship_eligibility(marks, attendance, age):
    """Check scholarship eligibility with boolean logic."""
    attendance_value = float(attendance)
    eligible = (marks >= 85 and attendance_value >= 90) and not (age < 18)
    return eligible


def adult_or_minor(age):
    """Use truthy and falsy checks in a simple helper."""
    if age:
        return "Adult" if age >= 18 else "Minor"
    return "Age not provided"


def show_menu():
    """Display a simple menu using match-case."""
    print("\nChoose an option:")
    print("1. Show grade")
    print("2. Show pass/fail")
    print("3. Check scholarship")
    print("4. Show adult/minor status")
    print("5. Quit")


def main():
    print("Welcome to the Student Result Checker")

    name, marks, age, attendance = get_student_details()

    if not name:
        print("Name cannot be empty.")
        return

    grade = calculate_grade(marks)
    result = determine_pass_fail(marks)
    scholarship = scholarship_eligibility(marks, attendance, age)
    category = adult_or_minor(age)

    print(f"\nStudent: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    print(f"Scholarship Eligible: {'Yes' if scholarship else 'No'}")
    print(f"Status: {category}")

    while True:
        show_menu()
        choice = safe_input("Enter your choice: ", "5")

        match choice:
            case "1":
                print(f"Grade: {grade}")
            case "2":
                print(f"Pass/Fail: {result}")
            case "3":
                print(f"Scholarship Eligible: {'Yes' if scholarship else 'No'}")
            case "4":
                print(f"Adult/Minor Status: {category}")
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Please choose a valid option.")


if __name__ == "__main__":
    main()
