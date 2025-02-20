# Sample data: 20 students with one-syllable names and their scores for 10 lessons
students = [
    {'name': 'Ben', 'scores': {'Math': 85, 'Music': 90, 'English': 88, 'History': 92, 'Geography': 84, 'Biology': 78, 'Physics': 80, 'Chemistry': 75, 'Art': 89, 'Physical Education': 91}},
    {'name': 'Dan', 'scores': {'Math': 76, 'Music': 82, 'English': 79, 'History': 81, 'Geography': 85, 'Biology': 77, 'Physics': 69, 'Chemistry': 80, 'Art': 82, 'Physical Education': 88}},
    {'name': 'Eve', 'scores': {'Math': 92, 'Music': 95, 'English': 94, 'History': 90, 'Geography': 89, 'Biology': 85, 'Physics': 91, 'Chemistry': 88, 'Art': 95, 'Physical Education': 96}},
    {'name': 'Max', 'scores': {'Math': 79, 'Music': 80, 'English': 82, 'History': 85, 'Geography': 78, 'Biology': 83, 'Physics': 81, 'Chemistry': 85, 'Art': 84, 'Physical Education': 87}},
    {'name': 'Sam', 'scores': {'Math': 88, 'Music': 89, 'English': 90, 'History': 86, 'Geography': 91, 'Biology': 84, 'Physics': 83, 'Chemistry': 79, 'Art': 85, 'Physical Education': 90}},
    {'name': 'Tom', 'scores': {'Math': 84, 'Music': 87, 'English': 86, 'History': 89, 'Geography': 82, 'Biology': 87, 'Physics': 79, 'Chemistry': 82, 'Art': 88, 'Physical Education': 85}},
    {'name': 'Ray', 'scores': {'Math': 82, 'Music': 85, 'English': 84, 'History': 87, 'Geography': 88, 'Biology': 79, 'Physics': 85, 'Chemistry': 83, 'Art': 82, 'Physical Education': 89}},
    {'name': 'Joe', 'scores': {'Math': 90, 'Music': 91, 'English': 92, 'History': 93, 'Geography': 87, 'Biology': 89, 'Physics': 91, 'Chemistry': 90, 'Art': 90, 'Physical Education': 93}},
    {'name': 'Zoe', 'scores': {'Math': 78, 'Music': 80, 'English': 76, 'History': 75, 'Geography': 79, 'Biology': 77, 'Physics': 76, 'Chemistry': 75, 'Art': 80, 'Physical Education': 81}},
    {'name': 'Kai', 'scores': {'Math': 91, 'Music': 93, 'English': 94, 'History': 90, 'Geography': 92, 'Biology': 89, 'Physics': 87, 'Chemistry': 90, 'Art': 91, 'Physical Education': 92}},
    {'name': 'Rob', 'scores': {'Math': 83, 'Music': 84, 'English': 86, 'History': 85, 'Geography': 80, 'Biology': 84, 'Physics': 81, 'Chemistry': 82, 'Art': 87, 'Physical Education': 85}},
    {'name': 'Meg', 'scores': {'Math': 86, 'Music': 88, 'English': 89, 'History': 87, 'Geography': 91, 'Biology': 88, 'Physics': 90, 'Chemistry': 87, 'Art': 90, 'Physical Education': 88}},
    {'name': 'Tim', 'scores': {'Math': 74, 'Music': 75, 'English': 78, 'History': 79, 'Geography': 80, 'Biology': 81, 'Physics': 72, 'Chemistry': 73, 'Art': 74, 'Physical Education': 75}},
    {'name': 'Jon', 'scores': {'Math': 82, 'Music': 84, 'English': 80, 'History': 83, 'Geography': 81, 'Biology': 84, 'Physics': 85, 'Chemistry': 82, 'Art': 80, 'Physical Education': 85}},
    {'name': 'Kim', 'scores': {'Math': 93, 'Music': 95, 'English': 94, 'History': 92, 'Geography': 91, 'Biology': 89, 'Physics': 93, 'Chemistry': 91, 'Art': 95, 'Physical Education': 94}},
    {'name': 'Lee', 'scores': {'Math': 80, 'Music': 82, 'English': 83, 'History': 84, 'Geography': 78, 'Biology': 85, 'Physics': 84, 'Chemistry': 83, 'Art': 82, 'Physical Education': 85}},
    {'name': 'Sue', 'scores': {'Math': 89, 'Music': 88, 'English': 90, 'History': 92, 'Geography': 87, 'Biology': 88, 'Physics': 90, 'Chemistry': 91, 'Art': 88, 'Physical Education': 91}},
    {'name': 'Ted', 'scores': {'Math': 76, 'Music': 77, 'English': 75, 'History': 74, 'Geography': 79, 'Biology': 78, 'Physics': 77, 'Chemistry': 76, 'Art': 77, 'Physical Education': 79}},
    {'name': 'Ann', 'scores': {'Math': 85, 'Music': 86, 'English': 84, 'History': 89, 'Geography': 87, 'Biology': 86, 'Physics': 85, 'Chemistry': 84, 'Art': 86, 'Physical Education': 88}},
    {'name': 'Jim', 'scores': {'Math': 81, 'Music': 82, 'English': 79, 'History': 80, 'Geography': 82, 'Biology': 81, 'Physics': 83, 'Chemistry': 80, 'Art': 81, 'Physical Education': 82}}
]

# Set KKM to 75
KKM = 75

lessons = [
    'Math', 'Music', 'English', 'History', 'Geography',
    'Biology', 'Physics', 'Chemistry', 'Art', 'Physical Education'
]

# Validate that the student name is a valid string containing only alphabetic characters
def validate_student_name(name):
    if name.isalpha():
        return True
    else:
        print("Invalid input: Name must consist of letters only.")
        return False

# Validate that the grade is a valid integer
def validate_grade_input(grade):
    try:
        grade = int(grade)
        return grade
    except ValueError:
        print("Invalid input: Grade must be a number.")
        return None

# Function to show student grades
def display_grades(student):
    print(f"\n{'-'*30}")
    print(f"{'Your Grades:':<15}")
    print(f"{'-'*30}")
    print(f"{'Subject':<15}{'Score':>10}")
    print(f"{'-'*30}")
    for lesson, score in student['scores'].items():
        if score is not None:
            print(f"{lesson:<15}{score:>10}")
        else:
            print(f"{lesson:<15}{'No grade recorded':>10}")
    print(f"{'-'*30}\n")

# Function to input student grades and handle invalid inputs with a limit of 3 attempts
def input_grade_for_student():
    attempts = 0
    while attempts < 3:
        student_name = input("Enter the student's name: ")
        
        # Validate student name
        if not validate_student_name(student_name):
            attempts += 1
            print(f"Invalid student name. {3 - attempts} attempts left.")
            continue

        lesson = input("Enter the lesson name: ")
        
        # Validate the lesson
        if lesson not in lessons:
            print(f"{lesson} is not a valid lesson.")
            attempts += 1
            print(f"{3 - attempts} attempts left.")
            continue

        # Check if the student exists in the data
        student = next((s for s in students if s['name'].lower() == student_name.lower()), None)
        if not student:
            print(f"No student found with the name {student_name}.")
            attempts += 1
            print(f"{3 - attempts} attempts left.")
            continue

        # Check if the student already has a grade for this lesson
        if lesson in student['scores']:
            print(f"{student_name} already has a grade for {lesson}: {student['scores'][lesson]}.")
            print("If you want to change the grade, please choose the correct option in the menu.")
            return

        # Validate grade input
        grade_input = input(f"Enter {student_name}'s grade for {lesson}: ")
        grade = validate_grade_input(grade_input)
        if grade is None:
            print(f"Invalid grade. {3 - attempts} attempts left.")
            attempts += 1
            continue
        
        # Assign the grade and break the loop
        student['scores'][lesson] = grade
        print(f"{student_name}'s grade for {lesson} has been recorded as {grade}.")
        break

    if attempts >= 3:
        print("Too many incorrect attempts. Restarting the process...")
        main_menu()

# Function to change an existing grade
def change_grade_for_student():
    attempts = 0
    while attempts < 3:
        student_name = input("Enter the student's name: ")
        
        # Validate student name
        if not validate_student_name(student_name):
            attempts += 1
            print(f"Invalid student name. {3 - attempts} attempts left.")
            continue

        # Check if the student exists
        student = next((s for s in students if s['name'].lower() == student_name.lower()), None)
        if not student:
            print(f"No student found with the name {student_name}.")
            attempts += 1
            print(f"{3 - attempts} attempts left.")
            continue

        lesson = input("Enter the lesson name: ")

        # Validate the lesson
        if lesson not in lessons:
            print(f"{lesson} is not a valid lesson.")
            attempts += 1
            print(f"{3 - attempts} attempts left.")
            continue

        # Check if the student has a grade for this lesson
        if lesson not in student['scores']:
            print(f"{student_name} does not have a recorded grade for {lesson}.")
            return

        new_grade_input = input(f"Enter the new grade for {student_name} in {lesson}: ")
        
        # Validate grade input
        new_grade = validate_grade_input(new_grade_input)
        if new_grade is None:
            print(f"Invalid grade. {3 - attempts} attempts left.")
            attempts += 1
            continue
        
        # Update the grade and break the loop
        student['scores'][lesson] = new_grade
        print(f"{student_name}'s grade for {lesson} has been updated to {new_grade}.")
        break

    if attempts >= 3:
        print("Too many incorrect attempts. Returning to the main menu...")
        main_menu()

# Function to display the rankings and students below KKM (default set to 75)
def view_ranks_and_students_below_kkm(student_data, lesson):
    sorted_students = sorted(student_data, key=lambda x: x['scores'][lesson], reverse=True)
    
    # Display the ranking in a table format for the selected lesson
    print(f"Rankings for {lesson}:")
    print(f"{'Rank':<5} | {'Name':<10} | {'Score':<5}")
    print("-" * 25)
    for rank, student in enumerate(sorted_students, start=1):
        print(f"{rank:<5} | {student['name']:<10} | {student['scores'][lesson]:<5}")
    
    print(f"\nStudents with scores below KKM ({lesson}, KKM={KKM}):")
    print(f"{'Name':<10} | {'Score':<5}")
    print("-" * 17)
    
    students_below_kkm = [student for student in sorted_students if student['scores'][lesson] < KKM]
    if students_below_kkm:
        for student in students_below_kkm:
            print(f"{student['name']:<10} | {student['scores'][lesson]:<5}")
    else:
        print("All students passed the KKM.")

# Function to erase all student grades for a new academic period
def erase_all_grades():
    confirmation = input("Are you sure you want to erase all grades? This action cannot be undone. (Yes/No): ")
    if confirmation.lower() == "yes":
        for student in students:
            student['scores'] = {lesson: None for lesson in lessons}
        print("All grades have been erased. You can now input new grades for the new academic period.")
    else:
        print("Operation canceled. No grades were erased.")

# Function to validate teacher's password
def validate_teacher_password():
    teacher_password = "ABC123"
    attempts = 0
    while attempts < 3:
        password = input("Enter the teacher's password: ")
        if password == teacher_password:
            print("Password accepted.")
            return True
        else:
            attempts += 1
            print(f"Wrong password. {3 - attempts} attempts left.")
    
    print("Too many incorrect attempts. You are locked out.")
    return False

# Main teacher menu function
def teacher_menu():
    if validate_teacher_password():
        attempts = 0  # Initialize attempts counter
        while attempts < 3:
            print("\nTeacher Menu:")
            print("1. View student ranks")
            print("2. Input grades")
            print("3. Change a student's grade")
            print("4. Erase all grades (New Academic Period)")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                lesson = input("Enter the lesson to view ranks: ")
                view_ranks_and_students_below_kkm(students, lesson)
                attempts = 0  # Reset attempts after a valid choice
            elif choice == "2":
                input_grade_for_student()
                attempts = 0  # Reset attempts after a valid choice
            elif choice == "3":
                change_grade_for_student()
                attempts = 0  # Reset attempts after a valid choice
            elif choice == "4":
                erase_all_grades()
                attempts = 0  # Reset attempts after a valid choice
            elif choice == "5":
                print("Exiting...")
                break
            else:
                attempts += 1
                print(f"Invalid choice, {3 - attempts} attempts left.")

            # If more than 3 invalid choices, exit to main menu
            if attempts >= 3:
                print("Too many invalid attempts. Returning to the main menu...")
                main_menu()
                break

def student_menu():
    attempts = 0  # Initialize attempts counter for student name validation

    # Attempt to validate student name
    while attempts < 3:
        student_name = input("Enter your name: ")
        if not validate_student_name(student_name):
            attempts += 1
            print(f"Invalid student name. {3 - attempts} attempts left.")
            continue
        
        # Find the student by name
        student = next((s for s in students if s['name'] == student_name), None)
        if not student:
            attempts += 1
            print(f"No student found with the name {student_name}. {3 - attempts} attempts left.")
            continue
        
        break  # Exit loop if student is found and name is valid

    if attempts >= 3:
        print("Too many invalid attempts. Returning to the main menu...")
        main_menu()
        return

    # Reset attempts for menu choices
    attempts = 0
    while attempts < 3:
        print(f"\nWelcome, {student_name}!")
        print("1. View your grades")
        print("2. View ranks for a specific lesson")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_grades(student)
            attempts = 0  # Reset attempts after a valid choice
        elif choice == "2":
            lesson = input("Enter the lesson to view ranks: ")
            if lesson in lessons:
                view_ranks_and_students_below_kkm(students, lesson)
                attempts = 0  # Reset attempts after a valid choice
            else:
                print(f"{lesson} is not a valid lesson.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            attempts += 1
            print(f"Invalid choice, {3 - attempts} attempts left.")

        # If more than 3 invalid choices, exit to main menu
        if attempts >= 3:
            print("Too many invalid attempts. Returning to the main menu...")
            main_menu()
            break

# Main menu function to start the program
def main_menu():
    print("Welcome to the Student Grade System!")
    attempts = 0  # Initialize attempts counter for main menu

    while attempts < 3:
        print("\nMain Menu:")
        print("1. Student")
        print("2. Teacher")
        role_choice = input("Are you a Student or Teacher? Enter your choice (1/2): ")

        if role_choice == "1":
            student_menu()
            attempts = 0  # Reset attempts after a valid choice
        elif role_choice == "2":
            teacher_menu()
            attempts = 0  # Reset attempts after a valid choice
        else:
            attempts += 1
            print(f"Invalid choice. {3 - attempts} attempts left.")
        
        if attempts >= 3:
            print("Too many invalid attempts. Exiting the system...")
            break

main_menu()