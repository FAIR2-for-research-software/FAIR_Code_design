"""
This script reads in data for students in a class and prints out the data in a table,
including their total score over three exercises.
It then calculates the average score for each exercise,
and finally prints the student with the highest overall total.
"""

### DO NOT MODIFY THIS DATA ###
# format: studentid,firstname,surname,score1,score2,score3
data = """39816,Fiona,Ellis,15,18,16
40859,Philip,Holdcroft,12,17,15
71625,Kathleen,Ingram,20,19,19
91462,David,Nicholson,14,16,18
97297,Mark,Walch,18,20,17"""
### DO NOT MODIFY THIS DATA ###


# 1) Check the data is formatted correctly
rows = data.split('\n')
for row in rows:
    fields = row.split(',')
    if len(fields) != 6:
        raise ValueError(f"This row does not have enough fields: {row}")
    if not fields[0].isdigit():
        raise ValueError(f"This row has an invalid studentid: {row}")
    if not fields[3].isdigit() or int(fields[3]) < 0 or int(fields[3]) > 20:
        raise ValueError(f"This row has an invalid score1: {row}")
    if not fields[4].isdigit() or int(fields[4]) < 0 or int(fields[4]) > 20:
        raise ValueError(f"This row has an invalid score2: {row}")
    if not fields[5].isdigit() or int(fields[5]) < 0 or int(fields[5]) > 20:
        raise ValueError(f"This row has an invalid score3: {row}")

# 2) Print out the data in a table
print("studentid  firstname  surname    score1  score2  score3  total ")
for row in rows:
    fields = row.split(',')
    studentid = fields[0]
    firstname = fields[1]
    surname = fields[2]
    score1 = fields[3]
    score2 = fields[4]
    score3 = fields[5]
    total_score = int(score1) + int(score2) + int(score3)
    print(f"{studentid:<10} {firstname:<10} {surname:<10} {score1:<7} {score2:<7} {score3:<7} {total_score:<7}")

# 3) Calculate the average of each score for the students
total_score1 = 0
total_score2 = 0
total_score3 = 0
count = 0
for row in rows:
    fields = row.split(',')
    score1 = int(fields[3])
    score2 = int(fields[4])
    score3 = int(fields[4])
    total_score1 += score1
    total_score2 += score2
    total_score3 += score3
    count += 1
average_score1 = total_score1 / count
average_score2 = total_score2 / count
average_score3 = total_score3 / count
print(f"Average score1: {average_score1:.2f}")
print(f"Average score2: {average_score2:.2f}")
print(f"Average score3: {average_score3:.2f}")

# 4) Find the student with the highest total score
highest_student = None
highest_score = 0
for row in rows:
    fields = row.split(',')
    firstname = fields[1]
    surname = fields[2]
    score1 = int(fields[3])
    score2 = int(fields[4])
    score3 = int(fields[5])
    total_score = int(score1) + int(score2) + int(score3)
    if total_score > highest_score:
        highest_score = total_score
        highest_student = f"{firstname} {surname}"
print(f"Student with highest total: {highest_student} ({highest_score:.2f})")
