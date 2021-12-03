import sys
names = sys.argv[1].strip().split(",")
student_records = {}
with open("student.txt") as records:
    for line in records:
        line = line.strip("\n  ")
        if len(line) == 0:  # pass empty line
            continue
        name, record = line.split(":")
        student_records[name] = record

try:
    for student in names:
        print("Name: {}, University: {}".format(student, student_records[student]), end=" ")

except KeyError:
    print("No record of '{}' was found".format(student), end=" ")