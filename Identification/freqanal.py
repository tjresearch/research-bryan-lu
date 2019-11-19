

f = open("finalizeprobs4.txt", "r")
alllines = f.readlines()
freqtable = {}
for line in alllines:
    wds = line.split()
    for wd in wds:
        wd = wd.replace(',', '')
        wd = wd.replace('.', '')
        if wd not in freqtable.keys():
            freqtable[wd] = 1
        else:
            freqtable[wd] += 1

freqlist = []
for key in freqtable.keys():
    freqlist.append((freqtable[key], key))
freqlist.sort()

stats = open("probstats2.txt", "w")
freqlist = freqlist[::-1]
for itm in freqlist:
    stats.write(itm[1] + " " + str(itm[0]) + "\n")
stats.close()
print(freqlist)