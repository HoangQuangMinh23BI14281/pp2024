import math

def get_input(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(f"{prompt}")
    stdscr.refresh()

    # Get the user input as a string
    user_input = ""
    while True:
        char = stdscr.getch()  # get a character
        if char == 10:  # Enter key is pressed
            break
        elif char == 27:  # Escape key (cancel)
            user_input = ""
            break
        elif char == 263:  # Backspace (delete last character)
            user_input = user_input[:-1]
        else:
            user_input += chr(char)  # Add the character to the input string

        # Display the current input in the window
        stdscr.clear()
        stdscr.addstr(f"{prompt}{user_input}")
        stdscr.refresh()

    return user_input

def save_students_to_file(students):
    with open('students.txt', 'w') as f:
        for student in students:
            f.write(f"{student.student_id},{student.name}\n")

def save_courses_to_file(courses):
    with open('courses.txt', 'w') as f:
        for course in courses:
            f.write(f"{course.course_id},{course.name},{course.credits}\n")

def save_marks_to_file(marks):
    with open('marks.txt', 'w') as f:
        for student_id, courses_marks in marks.items():
            for course_id, mark in courses_marks.items():
                f.write(f"{student_id},{course_id},{mark}\n")
