# Student Grade Calculator
# Week 2 Project

def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Keep practicing and improving! 📚"
    else:
        return "F", "Don't give up. Work harder and try again! 💪"


def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")

        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    print("=" * 40)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 40)

    student_name = input("Enter student name: ")

    marks = get_valid_marks()

    grade, message = get_grade(marks)

    print("\n📊 RESULT FOR", student_name.upper())
    print("-" * 40)
    print(f"Marks  : {marks}/100")
    print(f"Grade  : {grade}")
    print(f"Message: {message}")
    print("-" * 40)


main()