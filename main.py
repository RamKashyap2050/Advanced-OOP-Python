from classes import student
from exercise import Course
from random import randint


def add_random_grade(s: student):
    s.add_grades(randint(60, 100))


# with open('classlist.txt', 'a') as file:
#   file.write(str(Ram))

def main():
    oop = Course('OOP II', 'P02-P01')
    oop.add_students('Ram Kashyap', '0001')
    oop.add_students('Deepak', '0002')
    oop.add_students('Praneel', '0003')

    for student in oop.Students:
        for i in range(5):
            add_random_grade(student)
    print(oop)


if __name__ == '__main__':
    main()
