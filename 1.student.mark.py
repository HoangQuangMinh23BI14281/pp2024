def student_input():
    students = []
    number_students = int(input("Nhap so hoc sinh: "))
    for _ in range (number_students):
        student_id = input("nhap ma sinh vien: ")
        student_name = input("nhap ten sinh vien: ")
        students = students + [{"id": student_id, "name": student_name}]
    return students


def courses_input():
    courses = []
    number_courses = int(input("nhap so mon hoc: "))
    for _ in range (number_courses):
        course_id = input("nhap id mon hoc: ")
        course_name = input("nhap ten mon hoc: ")
        courses = courses + [{"id": course_id, "name": course_name}]
    return courses

def marks_input(students, courses):
    marks = {}
    for course in courses:
        for student in students:
            print("nhap diem cho hoc sinh: " + student["name"] + " cua mon " + course["name"] + ":")
            mark = float(input())
            if student["id"] not in marks:
                marks[student["id"]] = {}
                marks[student["id"]][course["id"]] = mark
    return marks

def studennt_list(students):
    for student in students:
        print("ID hoc sinh: " + student["id"] + " - Ten " + student["name"])

def course_list(courses):
    for course in courses:
        print("ID mon hoc: " + course["id"] + " - Ten mon hoc " + course["name"])

def Mark(courses, students, marks):
    for student in students:
        mark = "Khong co diem"
        for course in courses:
            if student["id"] in marks and course["id"] in marks[student["id"]]:
                mark = marks[student["id"]][course["id"]]
                break
        print(f"Ten: {student["name"]} - Diem: {mark}")

def main():
    students = student_input()
    courses = courses_input()
    marks = marks_input(students, courses)

    while True:
        print("\n 1. Xem thong tin mon hoc\n 2. Xem thong tin hoc sinh\n 3. Xem diem cua hoc sinh trong tung mon\n 4. Thoat")
        choice = input("Lua chon cua ban: ")

        if choice == "1":
            course_list(courses)
        elif choice == "2":
            studennt_list(students)
        elif choice == "3":
            course_id = input("nhap ma sinh vien: ")
            Mark(courses, students, marks)
        elif choice == "4":
            break

main()