from classroom import Classroom
from students import Student
import matplotlib.pyplot as plt

class Visualz :

    def __init__(self, class_name, student_list):
        self.cls = Classroom(class_name)
        self.cls.students_list = student_list

    def student_avg_visulaz(self):
        names = []
        avgs = []
        for student in self.cls.students_list:
            names.append(student.name)
            avgs.append(student.get_average())

        plt.figure()
        plt.barh(names, avgs, color="red")
        plt.title("Student Averages")

    def top_students(self):

        stu_dict = sorted(self.cls.students_list, key=lambda x: x.get_average(), reverse=True)[:5]

        top_5_name = [stu.name for stu in stu_dict]
        top_5_scores = [stu.get_total() for stu in stu_dict]

        plt.figure()
        plt.bar(top_5_name, top_5_scores, color="green")
        cuz = dict(
            fontweight="bold",
            fontfamily="Arial",
            fontsize=17
        )
        plt.title(
            "Top 5 Rank-Holders",
            color="red", **cuz
        )

        plt.xlabel("Students", color="grey",**cuz)
        plt.ylabel("Marks", color="black",**cuz)
        plt.show()

    def show_all_avg_subjects(self):
        subject = []
        avgs = []
        for student in self.cls.students_list:
            for subjects in student.marks:
                subject.append(subjects)

        unique = list(dict.fromkeys(subject))

        for subject in unique:
            avgs.append(self.cls.subject_average(subject))

        plt.figure()
        plt.bar(unique, avgs, color="black", width=0.5)
        plt.title(f"{self.cls.class_name} SA")
        plt.xlabel("Subjects")
        plt.ylabel("Marks")

        plt.show()














