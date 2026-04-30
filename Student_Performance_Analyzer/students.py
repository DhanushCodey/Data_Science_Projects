class Student:

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def get_total(self):
        return sum(self.marks.values())

    def get_average(self):
        num_subjects = int(len(self.marks))
        avg = round(self.get_total() / num_subjects, 1)

        return avg

    def get_grade_subjects(self):
        subject_gard = []
        for sub in self.marks.values():
            if sub >= 90:
                subject_gard.append('A')
            elif 80 <= sub < 90:
                subject_gard.append('B')
            elif 70 <= sub < 80:
                subject_gard.append('C')
            elif 51 <= sub < 70:
                subject_gard.append('D')
            else:
                subject_gard.append('F')
        return subject_gard

    def get_final_grade(self):
        total_score = self.get_average()
        if total_score >= 90 :
            return 'A'
        elif 80 <= total_score < 90:
            return 'B'
        elif 70 <= total_score < 80:
            return 'C'
        elif 51 <= total_score < 70:
            return 'D'
        else:
            return 'F'

    def display_info(self):
        print(
            f"ID          : {self.student_id} \n"
            f"Name        : {self.name} \n"
            f"Marks       : {self.marks} \n"
            f"Average     : {self.get_average()} \n"
            f"Sub-Grades  : {self.get_grade_subjects()} \n"
            f"Final-Grade : {self.get_final_grade()}"
        )
