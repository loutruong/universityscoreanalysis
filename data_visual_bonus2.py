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

name = []  # Danh sách các họ
name_count = []  # Số lần lặp của họ

for s in students:
    s_name = s[1].split(" ")
    firstname = s_name[-1]
    if firstname not in name:
        name.append(firstname)
        name_count.append(0)
        name_count[name.index(firstname)] += 1
    else:
        name_count[name.index(firstname)] += 1

print(name)
print(name_count)

counted_max_num = []  # Số lần lặp lại các họ từ lớn đến bé
sort_index = []  # Danh sách vị trí sau khi đã sắp xếp

# Tạo counted_max_num, danh sách số lần lặp các họ lớn nhất
for i in range(len(name)):
    max_number = 0
    for j in range(len(name)):
        if name_count[j] > max_number and name_count[j] not in counted_max_num:
            max_number = name_count[j]
    counted_max_num.append(max_number)

# Tạo sort_index, vị trí bằng cách tìm vị trí của các con số lớn nhất từ counted_max_num
for max_num in counted_max_num:
    for i in range(len(name)):
        if name_count[i] == max_num and i not in sort_index:
            sort_index.append(i)

name_sorted = []  # Danh sách họ đã sắp xếp
name_counted_sorted = []  # Danh sách số lần lặp mỗi họ đã sắp xếp

# Dùng sort_index để sắp xếp lại họ và số lần lặp
for index in sort_index:
    name_sorted.append(name[index])
    name_counted_sorted.append(name_count[index])

print(name_sorted)
print(name_counted_sorted)
print(len(name_counted_sorted))
# Draw
num = 30  # Số họ được vẽ

x = np.arange(num)
y = np.arange(num)

fig, axis = plt.subplots()
plt.bar(x, name_counted_sorted[0:num])

# label for column x
plt.xticks(x, name_sorted[0:num])

axis.set_ylabel('Số học sinh')

rects = axis.patches

# Make some labels.
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
labels = name_counted_sorted[0:num]
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2,
              height + 2, label, ha='center', va='bottom')

plt.title(str(num) + ' tên phố biến nhất trong kì thi')

plt.show()
