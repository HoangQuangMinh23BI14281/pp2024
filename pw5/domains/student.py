class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"ID: {self.student_id} - Ten: {self.name}"

    @staticmethod
    def from_file(line):
        student_id, name = line.strip().split(',')
        return Student(student_id, name)
