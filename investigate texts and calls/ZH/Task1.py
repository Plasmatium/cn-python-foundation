"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

all_number = set()
for rec in texts:
	all_number.add(rec[0])
	all_number.add(rec[1])

all_call_number = set()
for rec in calls:
	all_number.add(rec[0])
	all_number.add(rec[1])

print(f'There are {len(all_number)} different telephone numbers in the records')
