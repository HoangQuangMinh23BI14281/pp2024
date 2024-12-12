class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"ID: {self.student_id} - Name: {self.name}"

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.course_id} - Course: {self.name}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        number_students = int(input("Nhap so hoc sinh: "))
        for _ in range(number_students):
            student_id = input("Nhap ID hoc sinh: ")
            student_name = input("Nhap ten hoc sinh: ")
            self.students.append(Student(student_id, student_name))

    def input_courses(self):
        number_courses = int(input("Nhap so mon hoc "))
        for _ in range(number_courses):
            course_id = input("Nhap ID mon hoc: ")
            course_name = input("Nhap ten mon hoc:")
            self.courses.append(Course(course_id, course_name))

    def input_marks(self):
        for course in self.courses:
            for student in self.students:
                mark = float(input(f"Nhap diem cho Minh {student.name} trong {course.name}: "))
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
        for student in self.students:
            if student.student_id == student_id:
                print(f"Diem cua {student.name}:")
                for course in self.courses:
                    mark = self.marks.get(student.student_id, {}).get(course.course_id, "No mark")
                    print(f"{course.name}: {mark}")
                break

    def run(self):
        self.input_students()
        self.input_courses()
        self.input_marks()

        while True:
            print("\n1. Xem thong tin mon hoc\n2. Xem thong tin mon hoc\n3. Xem diem hoc sinh\n4. Thoat")
            choice = input("Your choice: ")

            if choice == "1":
                self.display_courses()
            elif choice == "2":
                self.display_students()
            elif choice == "3":
                self.display_marks()
            elif choice == "4":
                break

# Running the program
if __name__ == "__main__":
    school = School()
    school.run()
