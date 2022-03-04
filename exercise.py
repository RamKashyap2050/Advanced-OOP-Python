# Create a class called course. It should contain:
from classes import student


class Course:
    def __init__(self, title, course_id):
        self.title = title
        self.course_id = course_id
        self.Students = []

    def add_students(self, name, id):
        self.Students.append(student(name, id))

    def __str__(self):
        out = ''
        for s in self.Students:
            out += str(s) + "\n"
        return out
