from students import Student

class Classroom :

    def __init__(self, class_name):
        self.class_name = class_name
        self.students_list = []

    def add_student(self, student):
        self.students_list.append(student)
        return self.students_list

    def remove_student(self, id):
        index = 0
        for student in self.students_list :
            if id == student.student_id:
                break
            index += 1
        del self.students_list[index]

    def get_topper(self):
        topper = None
        initial_score = 0
        for student in self.students_list:
            score = student.get_total()
            if score > initial_score :
                initial_score = score
                topper = student
            else:
                continue
        return topper

    def get_class_average(self):
        total_class_score = 0
        for _ in self.students_list:
            total_class_score += _.get_total()
        class_avg = round(total_class_score / len(self.students_list), 1)
        return class_avg

    def subject_average(self, subject_name):
        subject_mark = 0
        for student in self.students_list:
            subject_mark += student.marks[subject_name]
        subject_average = round(subject_mark / len(self.students_list), 1)
        return subject_average

    def show_all_students(self):
        for student in self.students_list:
            student.display_info()

