class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = []

    def add_grades(self, grade):
        if grade >= 90:
            self.grades.append(4.0)
        elif grade >= 80:
            self.grades.append(3.0)
        elif grade >= 70:
            self.grades.append(2.0)
        elif grade >= 60:
            self.grades.append(1.0)
        else:
            self.grades.append(0.0)

    def get_gpa(self):
        return round(sum(self.grades) / len(self.grades), 2) if len(self.grades) > 0 else 0.0

    def __str__(self):
        return f"{self.id}, {self.name}, {self.get_gpa()}"
