import re
# f = open('geoproblems.txt', 'r+')
# out = open('cleanedprobs.txt', 'w+')
# statements = f.readlines()
# counter = 0
# for line in statements:
#     line.replace('90^{circ}', '90')
#     line.replace('{', ' ')
#     line.replace('}', ' ')
#     if line.isspace():
#         continue
#     words = line.split()
#     canonical = False
#     for wd in words:
#         if wd.isupper():
#             canonical = True
#             break
#     if canonical:
#         out.write(line)
#         counter += 1


# f = open('finalizedprobs.txt', 'r+')
# out = open('finalizeprobs2.txt', 'w+')
# statements = f.readlines()
# counter = 0
# for line in statements:
#     if line.isspace():
#         continue
#     words = line.split()
#     cleanLine = ""
#     for wd in words:
#         openbrace = wd.find("{")
#         closebrace = wd.find("}")
#         cleanwd = ""
#         for ch in wd:
#             if ch == '{' or ch == '}':
#                 continue
#             cleanwd += ch
#         cleanLine += cleanwd + " "
#     counter += 1
#     out.write(cleanLine + "\n")

f = open('finalizeprobs3.txt', 'r+')
#out = open('finalizeprobs4.txt', 'w+')
statements = f.readlines()
counter = 0
for line in statements:
    if line.isspace():
        continue
    words = line.split()
    cleanLine = ""
    for wd in words:
        tempWd = wd
        plus = wd.find('+')
        if plus != -1 and wd != '+':
            newWd = tempWd[0:plus] + ' + ' + tempWd[plus+1:]
            tempWd = newWd
        equal = wd.find('=')
        if equal != -1 and wd != '=':
            newWd = tempWd[0:equal] + ' = ' + tempWd[equal+1:]
            tempWd = newWd
        lt = wd.find('<')
        if lt != -1 and wd != '<':
            newWd = tempWd[0:lt] + ' < ' + tempWd[lt+1:]
            tempWd = newWd
        gt = wd.find('>')
        if gt != -1 and wd != '>':
            newWd = tempWd[0:gt] + ' > ' + tempWd[gt+1:]
            tempWd = newWd
        times = wd.find('cdot')
        if times != -1 and wd != 'cdot':
            newWd = tempWd[0:times] + ' > ' + tempWd[times+4:]
            tempWd = newWd
        geq = wd.find('geq')
        if geq != -1 and wd != 'geq':
            newWd = tempWd[0:geq] + ' geq ' + tempWd[geq+3:]
            tempWd = newWd
        leq = wd.find('leq')
        if leq != -1 and wd != 'leq':
            newWd = tempWd[0:leq] + ' leq ' + tempWd[leq+3:]
            tempWd = newWd
        cap = wd.find('cap')
        if cap != -1 and wd != 'cap':
            newWd = tempWd[0:cap] + ' cap ' + tempWd[cap+3:]
            tempWd = newWd
        div = wd.find('/')
        if div != -1 and wd != '/':
            newWd = tempWd[0:div] + ' / ' + tempWd[div+1:]
            tempWd = newWd
        cleanLine += tempWd + ' '
    counter += 1
    #out.write(cleanLine + "\n")

f.close()
#out.close()
print(counter)
