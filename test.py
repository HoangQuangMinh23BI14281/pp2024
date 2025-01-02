import math
import numpy
import curses

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"ID: {self.student_id} - Ten: {self.name}"

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"ID: {self.course_id} - Mon: {self.name}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self, stdscr):
        number_students = self.get_input(stdscr, "Nhap so hoc sinh muon them: ")
        number_students = int(number_students)
        stdscr.clear()
        stdscr.addstr("\nDanh sach hoc sinh hien tai:\n")
        self.display_students(stdscr)
        for i in range(1, number_students+1):
            student_id = self.get_input(stdscr, f"Nhap ID hoc sinh {i}: ")
            student_name = self.get_input(stdscr, f"Nhap ten hoc sinh {i}: ")
            self.students.append(Student(student_id, student_name))
            self.input_marks_for_new_students([student_id], stdscr)
        stdscr.clear()
        stdscr.addstr("\nDanh sach hoc sinh hien tai:\n")
        self.display_students(stdscr)

    def input_courses(self, stdscr):
        number_courses = self.get_input(stdscr, "Nhap so mon hoc muon them: ")
        number_courses = int(number_courses)
        stdscr.clear()
        stdscr.addstr("\nDanh sach mon hoc hien tai:\n")
        self.display_courses(stdscr)
        for i in range(1, number_courses+1):
            course_id = self.get_input(stdscr, f"Nhap ID mon hoc {i}: ")
            course_name = self.get_input(stdscr, f"Nhap ten mon hoc {i}: ")
            credits = self.get_input(stdscr, f"Nhap so tin chi cua mon hoc: ")
            credits = int(credits)
            self.courses.append(Course(course_id, course_name, credits))
            self.input_marks_for_new_course(course_id, stdscr)
        stdscr.clear()
        stdscr.addstr("\nDanh sach mon hoc hien tai:\n")
        self.display_courses(stdscr)

    def input_marks_for_new_students(self, new_student_ids, stdscr):
        for student_id in new_student_ids:
            for course in self.courses:
                mark = self.get_input(stdscr, f"Nhap diem cho {self.get_student_name(student_id)} trong {course.name}: ")
                mark = float(mark)
                mark = math.floor(mark * 10) / 10
                if student_id not in self.marks:
                    self.marks[student_id] = {}
                self.marks[student_id][course.course_id] = mark

    def input_marks_for_new_course(self, new_course_id, stdscr):
        for student in self.students:
            mark = self.get_input(stdscr, f"Nhap diem cho {student.name} cho mon {self.get_course_name(new_course_id)}: ")
            mark = float(mark)
            mark = math.floor(mark * 10) / 10
            if student.student_id not in self.marks:
                self.marks[student.student_id] = {}
            self.marks[student.student_id][new_course_id] = mark

    def get_student_name(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student.name
        return "Unknown Student"

    def get_course_name(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course.name
        return "Unknown Course"

    def display_students(self, stdscr):
        for student in self.students:
            stdscr.addstr(f"{student}")
        stdscr.refresh()

    def display_courses(self, stdscr):
        for course in self.courses:
            stdscr.addstr(f"{course}\n")
        stdscr.refresh()

    def display_marks(self, stdscr):
        student_id = self.get_input(stdscr, "Nhap ID hoc sinh muon xem diem:")
        student_found = False
        for student in self.students:
            if student.student_id == student_id:
                student_found = True
                stdscr.addstr(f"\nDiem cua {student.name} trong mon ")
                for course in self.courses:
                    mark = self.marks[student_id].get(course.course_id, None)
                    if mark is not None:
                        stdscr.addstr(f"{course.name}: {mark}\n")
                    else:
                        stdscr.addstr(f"{course.name}: khong co diem\n")
                break
        if not student_found:
            stdscr.addstr("hoc sinh khong ton tai\n")
        stdscr.refresh()

    def GPA(self, student_id):
        total_credits = 0
        weighted_sum = 0

        if student_id not in self.marks:
            return 0
        
        for course in self.courses:
            mark = self.marks[student_id].get(course.course_id, None)
            if mark is not None:
                weighted_sum += mark * course.credits
                total_credits += course.credits

        if total_credits != 0:
            gpa = weighted_sum / total_credits
            return gpa
        else:
            return 0
    
    def sort_GPA(self, stdscr):
        student_gpa = []
        for student in self.students:
            gpa = self.GPA(student.student_id)
            student_gpa.append((student, gpa))

        sorted_array = numpy.sort(numpy.array(student_gpa, dtype=[('student', object), ('gpa', float)]), order='gpa')[::-1]
        
        stdscr.clear()
        for entry in sorted_array:
            student, gpa = entry
            stdscr.addstr(f"{student.name} - GPA: {gpa:.2f}\n")
        stdscr.refresh()

    def get_input(self, stdscr, prompt):
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

    def run(self, stdscr):

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "1. Them hoc sinh")
            stdscr.addstr(1, 0, "2. Them mon hoc")
            stdscr.addstr(2, 0, "3. Xem diem hoc sinh")
            stdscr.addstr(3, 0, "4. Xep diem hoc sinh theo GPA")
            stdscr.addstr(4, 0, "5. Xem thong tin hoc sinh")
            stdscr.addstr(5, 0, "6. Xem thong tin mon hoc")
            stdscr.addstr(6, 0, "7. Thoat")
            stdscr.addstr(7, 0, "Your choice: ")
            stdscr.refresh()

            choice = stdscr.getch()

            if choice == ord('1'):
                self.input_students(stdscr)
            elif choice == ord('2'):
                self.input_courses(stdscr)
            elif choice == ord('3'):
                self.display_marks(stdscr)
            elif choice == ord('4'):
                self.sort_GPA(stdscr)
            elif choice == ord('5'):
                self.display_students(stdscr)
            elif choice == ord('6'):
                self.display_courses(stdscr)
            elif choice == ord('7'):
                break
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(lambda stdscr: School().run(stdscr))
