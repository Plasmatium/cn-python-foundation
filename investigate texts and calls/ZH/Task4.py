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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

all_from_140 = [rec[0] for rec in calls if rec[0].startswith('140')]
all_recieve_calls = [rec[1] for rec in calls]
all_recieve_texts = [rec[1] for rec in texts]
all_send_texts = [rec[0] for rec in texts]

suspecious = sorted(
    set([num for num in all_from_140 if num not in all_recieve_texts and num not in all_recieve_calls and num not in all_send_texts]))

print('These numbers could be telemarketers: ')
[print('\t', s) for s in suspecious]
