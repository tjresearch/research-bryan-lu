import codecs
import random
# f = open("newproblems4.txt", encoding='utf-8', mode="r+")
#
# outfile = open("newproblems5.txt", encoding='utf-8', mode="w+")
# for line in f:
#     if line.isspace():
#         continue
#     if line.find("Iran") != -1:
#         continue
#     words = line.split(' ')
#     if words[0] == 'by':
#         continue
#     else:
#         outfile.write(line)

f = open("newproblems5.txt", encoding='utf-8', mode="r+")
outfile = open("prelimcases.txt", encoding='utf-8', mode="w+")
counter = 0
# for line in f:
#     counter += 1
# print(counter) ## 216 ## 67 ## 122
# f.close()
lines = [line for line in f]
for i in range(15):
    randomindex = random.randint(0, 120)
    outfile.write(lines[randomindex])
