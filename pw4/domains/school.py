import math
import numpy
from .student import Student
from .course import Course

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self, stdscr, get_input):
        number_students = get_input(stdscr, "Nhap so hoc sinh muon them: ")
        number_students = int(number_students)
        stdscr.clear()
        stdscr.addstr("\nDanh sach hoc sinh hien tai:\n")
        self.display_students(stdscr)
        for i in range(1, number_students + 1):
            student_id = get_input(stdscr, f"Nhap ID hoc sinh {i}: ")
            student_name = get_input(stdscr, f"Nhap ten hoc sinh {i}: ")
            self.students.append(Student(student_id, student_name))
            self.input_marks_for_new_students([student_id], stdscr, get_input)
        stdscr.clear()
        stdscr.addstr("\nDanh sach hoc sinh hien tai:\n")
        self.display_students(stdscr)

    def input_courses(self, stdscr, get_input):
        number_courses = get_input(stdscr, "Nhap so mon hoc muon them: ")
        number_courses = int(number_courses)
        stdscr.clear()
        stdscr.addstr("\nDanh sach mon hoc hien tai:\n")
        self.display_courses(stdscr)
        for i in range(1, number_courses + 1):
            course_id = get_input(stdscr, f"Nhap ID mon hoc {i}: ")
            course_name = get_input(stdscr, f"Nhap ten mon hoc {i}: ")
            credits = get_input(stdscr, f"Nhap so tin chi cua mon hoc: ")
            credits = int(credits)
            self.courses.append(Course(course_id, course_name, credits))
            self.input_marks_for_new_course(course_id, stdscr, get_input)
        stdscr.clear()
        stdscr.addstr("\nDanh sach mon hoc hien tai:\n")
        self.display_courses(stdscr)

    def input_marks_for_new_students(self, new_student_ids, stdscr, get_input):
        for student_id in new_student_ids:
            for course in self.courses:
                mark = get_input(stdscr, f"Nhap diem cho {self.get_student_name(student_id)} trong {course.name}: ")
                mark = float(mark)
                mark = math.floor(mark * 10) / 10
                if student_id not in self.marks:
                    self.marks[student_id] = {}
                self.marks[student_id][course.course_id] = mark

    def input_marks_for_new_course(self, new_course_id, stdscr, get_input):
        for student in self.students:
            mark = get_input(stdscr, f"Nhap diem cho {student.name} cho mon {self.get_course_name(new_course_id)}: ")
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

    def display_marks(self, stdscr, get_input):
        student_id = get_input(stdscr, "Nhap ID hoc sinh muon xem diem:")
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
