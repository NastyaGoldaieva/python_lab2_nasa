class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self, max_marks_per_subject):
        max_total_marks = max_marks_per_subject * len(self.marks)
        return (self.total_marks() / max_total_marks) * 100 if max_total_marks > 0 else 0


if __name__ == '__main__':
    student1 = Student("Alis")
    student1.add_mark(subject="math", mark=70)
    student1.add_mark(subject="eng", mark=80)
    print(f"total_marks: {student1.total_marks()}")
    print(f"percentage: {student1.percentage(100)}%")