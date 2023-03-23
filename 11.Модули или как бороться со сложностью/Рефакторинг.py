class Student:
    def __init__(self, name, group, course):
        self.name = name
        self.group = group
        self.course = course
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def get_avg_grade(self):
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count

class Group:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_avg_grade(self):
        total = sum(student.get_avg_grade() for student in self.students)
        count = len(self.students)
        return total / count

class Course:
    def __init__(self, number):
        self.number = number
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def get_avg_grade(self):
        total = sum(group.get_avg_grade() for group in self.groups)
        count = len(self.groups)
        return total / count

class Report:
    def __init__(self, courses):
        self.courses = courses

    def get_top_students(self, n):
        all_students = []
        for course in self.courses:
            for group in course.groups:
                all_students += group.students
        all_students.sort(key=lambda student: student.get_avg_grade(), reverse=True)
        return all_students[:n]

    def get_bottom_students(self, n):
        all_students = []
        for course in self.courses:
            for group in course.groups:
                all_students += group.students
        all_students.sort(key=lambda student: student.get_avg_grade())
        return all_students[:n]

    def get_top_subjects(self, n):
        all_grades = {}
        for course in self.courses:
            for group in course.groups:
                for student in group.students:
                    for subject, grades in student.grades.items():
                        if subject in all_grades:
                            all_grades[subject] += grades
                        else:
                            all_grades[subject] = grades
        avg_grades = {subject: sum(grades) / len(grades) for subject, grades in all_grades.items()}
        top_subjects = sorted(avg_grades.items(), key=lambda x: x[1], reverse=True)
        return top_subjects[:n]
