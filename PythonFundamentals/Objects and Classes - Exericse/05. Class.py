class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        avg = f"{sum(self.grades) / len(self.grades):.2f}"
        return float(avg)

    def __repr__(self):
        avg = sum(self.grades) / len(self.grades)
        return f"The students in {self.name}: " \
               f"{', '.join(self.students)}. Average grade: {avg:.2f}"