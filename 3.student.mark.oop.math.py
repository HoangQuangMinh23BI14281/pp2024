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

    def input_students(self):
        number_students = int(input("Nhap so hoc sinh: "))
        for i in range(1, number_students+1):
            student_id = input(f"Nhap ID hoc sinh {i}: ")
            student_name = input(f"Nhap ten hoc sinh {i}: ")
            self.students.append(Student(student_id, student_name))

    def input_courses(self):
        number_courses = int(input("Nhap so mon hoc: "))
        for i in range(1, number_courses+1):
            course_id = input(f"Nhap ID mon hoc {i}: ")
            course_name = input(f"Nhap ten mon hoc {i}: ")
            credits = int(input(f"Nhap so tin chi cua mon hoc: "))
            self.courses.append(Course(course_id, course_name, credits))

    def input_marks(self):
        for course in self.courses:
            for student in self.students:
                mark = float(input(f"Nhap diem cho {student.name} trong {course.name}: "))
                mark = math.floor(mark*10)/10 
                if student.student_id not in self.marks:
                    self.marks[student.student_id] = {}
                self.marks[student.student_id][course.course_id] = mark

    def display_students(self):
        for student in self.students:
            print(student)

    def display_courses(self):
        for course in self.courses:
            print(course)

    def display_marks(self):
        student_id = input("Nhap ID hoc sinh muon xem diem: ")
        student_found = False
        for student in self.students:
            if student.student_id == student_id:
                student_found = True
                print(f"Diem cua {student.name}:")
                for course in self.courses:
                    mark = self.marks[student_id].get(course.course_id, None)
                    if mark is not None:
                        print(f"{course.name}: {mark}")
                    else:
                        print(f"{course.name}: khong co diem")
                break
        if not student_found:
            print("hoc sinh khong ton tai")

    def GPA(self, student_id):
        total_credits = 0
        weighted_sum = 0

        if student_id not in self.marks:
            print("khong co hoc sinh")
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
    
    def sort_GPA(self):
        student_gpa = []
        for student in self.students:
            gpa = self.GPA(student.student_id)
            student_gpa.append((student, gpa))

        sorted_array = numpy.sort(numpy.array(student_gpa, dtype=[('student', object), ('gpa', float)]), order='gpa')[::-1]

        for entry in sorted_array:
            student, gpa = entry
            print(f"{student.name} - GPA: {gpa:.2f}")

    def run(self):
        self.input_students()
        self.input_courses()
        self.input_marks()

        while True:
            print("\n1. Xem thong tin mon hoc\n2. Xem thong tin hoc sinh\n3. Xem diem hoc sinh\n4. Xep diem hoc sinh theo GPA\n5. Thoat")
            choice = input("Your choice: ")

            if choice == "1":
                self.display_courses()
            elif choice == "2":
                self.display_students()
            elif choice == "3":
                self.display_marks()
            elif choice == "4":
                self.sort_GPA()
            elif choice == "5":
                break

if __name__ == "__main__":
    school = School()
    school.run()
