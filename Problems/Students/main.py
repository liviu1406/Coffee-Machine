class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = min(name) + '' + last_name + '' + str(birth_year)


first_name = input()
last_name = input()
year = input()
student = Student(first_name, last_name, year)
print(student.student_id)
