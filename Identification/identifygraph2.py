import nltk
problem = '''Let Gamma be the circumcircle of acute triangle ABC. Points D and E are on segments AB and AC respectively
            such that AD = AE. The perpendicular bisectors of BD and CE intersect minor arcs AB and AC of Gamma at
            points F and G respectively. Prove that lines DE and FG are either parallel or they are the same line.'''

badpuncts = ['.', ',']
greek = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu',
         'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
types = ['bool', 'num', 'var']
def removePunct(string):
    newstring = ''
    for ch in string:
        if ch in badpuncts:
            continue
        else:
            newstring += ch
    return newstring

# read in info from lexicon.txt ############

words = removePunct(problem).split()
geothings = open("lexicon.txt", 'r+')
allObjects = geothings.readlines()
detectables = {}
for line in allObjects:
    line = line.strip()
    associates = line.split(' ')
    critIndex = 0
    lookFor = []
    for i in range(len(associates)):
        if associates[i] != ':':
            lookFor.append(associates[i])
            continue
        else:
            critIndex = i
            break
    word = ' '.join(lookFor)
    detectables[word] = associates[critIndex+1:]

doubleWords = []
for key in detectables.keys():
    if key.find(" ") != -1:
        doubleWords.append(key)
explicit = []
detectObj = []

# /////////// FIND EXPLICIT VARIABLES, OBJECTS //////////////

for wd in words:
    if wd.isupper():
        explicit.append(wd)
    elif wd.lower() in greek:
        explicit.append(wd)
    if wd.find('_') != -1:
        if wd[:wd.find('_')].lower() in greek:
            explicit.append(wd)
    else:
        for obj in detectables.keys():
            if wd.find(obj) != -1:
                detectObj.append(obj)

# ///////////// FIND CONCEPTS WITH TWO-WORD CONCEPTS, I.E. PERPENDICULAR BISECTOR
for wd in doubleWords:
    newprob = problem
    while newprob.find(wd) != -1:
        idx = newprob.find(wd)
        detectObj.append(wd)
        newprob = newprob[idx+1:]

concepts = {}
for obj in detectObj:
    associates = detectables[obj]
    for wd in associates:
        if wd not in concepts.keys():
            concepts[wd] = 1
        else:
            concepts[wd] += 1

print(explicit)
print(detectObj)
print(concepts)

# PART OF SPEECH TAGGING #############
tokens = nltk.word_tokenize(problem)
partsSpeech = nltk.pos_tag(tokens)
print(partsSpeech)
# for the most part, we want NN (nouns and their variants), JJ (adjectives), VB (verbs), adverbs?

# DISTANCE IN SENTENCE - explicit ////////////
tempWds = [i for i in words]
explicitIdxs = []
detectedIdxs = []
expctr = 0
detctr = 0

for idx in range(len(tempWds)):
    if tempWds[idx] == explicit[expctr]:
        explicitIdxs.append((explicit[expctr], idx))
        expctr += 1
    if expctr == len(explicit):
        break

print(explicitIdxs)

for idx in range(len(tempWds)):
    for obj in detectables.keys():
        if tempWds[idx].find(obj) != -1:
            detectedIdxs.append((obj, idx))
    if idx != len(tempWds) - 1:
        possibleDouble = tempWds[idx] + ' ' + tempWds[idx+1]
        for phr in doubleWords:
            if possibleDouble.find(phr) != -1:
                detectedIdxs.append((phr, idx+0.5))

print(detectedIdxs)
#print(len(detectObj) == len(detectedIdxs))
# for each explicit variable:
# find its index in the sentence
# for each trigger geo word: same thing as above:
# create two maps, and then accessible easily

# DISTANCE IN TREE??? ///////////
# classification tree of objects, based on what kind of stuff they are... objects that are close in nature should be
# close together, etc. group explicit stuff together, group lines/segments, arcs and circles, closed shapes...
## do ordering manually while parsing right before the
# def getSign(obj1, obj2):
#     sign = 1
#     #if obj1 in explicitIdxs.keys():


def getDependencyTreeDist(obj1, obj2):  # between 0 and 3
    if obj1 in explicit and obj2 in explicit:
        return (len(obj1) - len(obj2))/10  # length diff * 0.1
    if obj1 in explicit and obj2 in detectables.keys():
        return 3
    elif obj2 in explicit and obj1 in detectables.keys():
        return 3
    else:
        associated1 = detectables[obj1]
        associated2 = detectables[obj2]
        notloops = ["point", "line", "segment", "angle", "bisector", "ray", "arc", "median", "altitude",
                    "angle bisector", "perpendicular bisector", "midpoint", "diameter", "radius"]
        if obj1 in notloops and obj2 not in notloops:
            return 2
        elif obj2 in notloops and obj1 not in notloops:
            return 2

        common = sum([1 for conc in associated1 if conc in associated2])
        return 1.4 - common/10


# UNARY/BINARY/TERNARY CLASSIFICATION ////////////////
# make txt file of relations and specify what relations are unary/binary, as well as return type
# allRels = open('finalrelations.txt', 'w+')
# rels = []
# for wd in detectables.keys():
#     for mapped in detectables[wd]:
#         if mapped[0].upper() == mapped[0] and mapped not in rels:
#             rels.append(mapped)
# for rel in rels:
#     allRels.write(rel + '\n')

# DATA TYPES FOR INPUTS, RETURN TYPES FOR RELATIONS /////////////
# types: bool num var

relfile = open("finalrelations.txt", 'r+')
relin = relfile.readlines()
reldict = {}
for line in relin:
    line = line.strip()
    relinfo = line.split()
    for wd in relinfo[2:]:
        if wd not in types:
            print("uh oh")
            break
    name = relinfo[0]
    numparams = relinfo[1]
    returntype = relinfo[2]
    intypes = relinfo[3:]
    reldict[name] = (numparams, returntype, intypes)

print(reldict)
