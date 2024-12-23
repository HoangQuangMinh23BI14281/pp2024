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
        number_students = int(self.get_input(stdscr, "Nhap so hoc sinh: "))
        for i in range(1, number_students+1):
            student_id = self.get_input(stdscr, f"Nhap ID hoc sinh {i}: ")
            student_name = self.get_input(stdscr, f"Nhap ten hoc sinh {i}: ")
            self.students.append(Student(student_id, student_name))

    def input_courses(self, stdscr):
        number_courses = int(self.get_input(stdscr, "Nhap so mon hoc: "))
        for i in range(1, number_courses+1):
            course_id = self.get_input(stdscr, f"Nhap ID mon hoc {i}: ")
            course_name = self.get_input(stdscr, f"Nhap ten mon hoc {i}: ")
            credits = int(self.get_input(stdscr, f"Nhap so tin chi cua mon hoc: "))
            self.courses.append(Course(course_id, course_name, credits))

    def input_marks(self, stdscr):
        for course in self.courses:
            for student in self.students:
                mark = float(self.get_input(stdscr, f"Nhap diem cho {student.name} trong {course.name}: "))
                mark = math.floor(mark*10)/10 
                if student.student_id not in self.marks:
                    self.marks[student.student_id] = {}
                self.marks[student.student_id][course.course_id] = mark

    def display_students(self, stdscr):
        stdscr.clear()
        for student in self.students:
            stdscr.addstr(f"{student}\n")
        stdscr.refresh()
        stdscr.getch()

    def display_courses(self, stdscr):
        stdscr.clear()
        for course in self.courses:
            stdscr.addstr(f"{course}\n")
        stdscr.refresh()
        stdscr.getch()

    def display_marks(self, stdscr):
        student_id = self.get_input(stdscr, "Nhap ID hoc sinh muon xem diem: ")
        student_found = False
        for student in self.students:
            if student.student_id == student_id:
                student_found = True
                stdscr.addstr(f"\nDiem cua {student.name}:\n")
                for course in self.courses:
                    mark = self.marks[student_id].get(course.course_id, None)
                    if mark is not None:
                        stdscr.addstr(f"{course.name}: {mark}\n")
                    else:
                        stdscr.addstr(f"{course.name}: khong co diem\n")
                stdscr.refresh()
                stdscr.getch()
                break
        if not student_found:
            stdscr.addstr("Hoc sinh khong ton tai\n")
            stdscr.refresh()
            stdscr.getch()

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
        stdscr.getch()

    def get_input(self, stdscr, prompt):
        stdscr.clear()
        stdscr.addstr(prompt)
        stdscr.refresh()
        input_str = ""
        while True:
            key = stdscr.getch()
            if key == 10:  # Enter key
                break
            elif key == 27:  # Escape key
                return ""
            elif key == 263:  # Backspace key
                input_str = input_str[:-1]
            else:
                input_str += chr(key)
            stdscr.clear()
            stdscr.addstr(prompt + input_str)
            stdscr.refresh()
        return input_str

    def run(self, stdscr):
        self.input_students(stdscr)
        self.input_courses(stdscr)
        self.input_marks(stdscr)

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "1. Xem thong tin mon hoc")
            stdscr.addstr(1, 0, "2. Xem thong tin hoc sinh")
            stdscr.addstr(2, 0, "3. Xem diem hoc sinh")
            stdscr.addstr(3, 0, "4. Xep diem hoc sinh theo GPA")
            stdscr.addstr(4, 0, "5. Thoat")
            stdscr.addstr(5, 0, "Your choice: ")
            stdscr.refresh()

            choice = stdscr.getch()

            if choice == ord('1'):
                self.display_courses(stdscr)
            elif choice == ord('2'):
                self.display_students(stdscr)
            elif choice == ord('3'):
                self.display_marks(stdscr)
            elif choice == ord('4'):
                self.sort_GPA(stdscr)
            elif choice == ord('5'):
                break
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(lambda stdscr: School().run(stdscr))
