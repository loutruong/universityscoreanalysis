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

# Number of Subject have been taken
num_of_exam_taken = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in students:
    count = 0
    for i in range(11):
        if s[i+5] != "-1":
            count += 1

        if count == 11:
            print(s)

        num_of_exam_taken[count] += 1

print(num_of_exam_taken)

# Draw pie chart
labels = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"
sizes = [0, 80, 122, 2598, 4334, 318, 2730, 64261, 0, 0, 0, 1]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.show()
