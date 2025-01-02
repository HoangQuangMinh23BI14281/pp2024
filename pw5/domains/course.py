class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"ID: {self.course_id} - Mon: {self.name}"

    @staticmethod
    def from_file(line):
        course_id, name, credits = line.strip().split(',')
        return Course(course_id, name, int(credits))
