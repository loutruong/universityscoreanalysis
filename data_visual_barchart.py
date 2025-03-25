import matplotlib.pyplot as plt
import numpy as np

# Read file
with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

# Remove last student (Empty student list)
students.pop()

# Total Number of Students
total_students = len(students)

# Split header
header = header.split(",")
subject = header[5:]

# Split student
for i in range(len(students)):
    students[i] = students[i].split(",")

not_take_exam = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Scan through all student
for s in students:
    # Iterate through all subject
    for i in range(5, 16):
        if s[i] == "-1":
            not_take_exam[i-5] += 1

not_take_exam_percentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 11):
    not_take_exam_percentage[i] = round(not_take_exam[i]/total_students*100, 2)

# Plot Barchart
figure, axis = plt.subplots()
plt.bar(subject, not_take_exam_percentage)
axis.set_ylim(0, 100)

plt.ylabel('Phần trăm')
plt.title('Số học sinh không đi thi hoặc không đăng kí')

# Draw number of student on top of each bar
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2,
              height + 2, label, ha='center', va='bottom')

plt.show()
