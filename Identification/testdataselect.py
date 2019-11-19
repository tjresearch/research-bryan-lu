import random

random.seed(17)
problemindices = []
for i in range(25):
    index = int(random.uniform(0,257))
    problemindices.append(index)

out = open("testdata.txt", "w+")
f = open("finalizeprobs4.txt", "r+")
problems = f.readlines()

for ind in problemindices:
    out.write(problems[ind])

f.close()
out.close()
