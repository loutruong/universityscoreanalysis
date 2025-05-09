import numpy as np
import matplotlib.pyplot as plt

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

# number of students who took 0,1,2,3,... subjects
num_of_exam_taken = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
average = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in students:
    count = 0
    total = 0
    for i in range(11):
        if s[i+5] != "-1":
            total += float(s[i+5])
            count += 1

    num_of_exam_taken[count] += 1
    average[count] += total/count

for i in range(12):
    if num_of_exam_taken[i] != 0:
        average[i] = round(average[i]/num_of_exam_taken[i], 2)

print(num_of_exam_taken)
print(average)

# Draw
x = np.arange(12)
y = np.arange(12)
print(x)

fig, axis = plt.subplots()
plt.bar(x, average)

# set limit
axis.set_ylim(0, 10)

# label for column x
plt.xticks(x, y)

axis.set_ylabel('Điểm Trung Bình')
axis.set_xlabel('Số môn thi')

rects = axis.patches

# Make some labels.
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
labels = average
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2,
              height, label, ha='center', va='bottom')

plt.title('Điểm trung bình theo số lượng môn thi')

plt.show()
