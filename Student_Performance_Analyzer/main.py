from classroom import Classroom
from students import Student
from visulaization import Visualz
import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")
data = df.to_dict(orient="records")

student_list = []

for info in data:
    marks = {k : int(v) for k,v in info.items() if k not in ["ID", "Name"]}
    stu = Student(info["ID"], info["Name"], marks)
    student_list.append(stu)

class_A2 = Classroom("A2")
class_A2.students_list = student_list

v = Visualz(class_A2.class_name, class_A2.students_list)
#
# v.student_avg_visulaz()
# v.top_students()

v.show_all_avg_subjects()
