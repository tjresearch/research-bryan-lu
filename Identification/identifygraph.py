problem = '''Let Gamma be the circumcircle of acute triangle ABC. Points D and E are on segments AB and AC respectively
            such that AD = AE. The perpendicular bisectors of BD and CE intersect minor arcs AB and AC of Gamma at
            points F and G respectively. Prove that lines DE and FG are either parallel or they are the same line.'''

badpuncts = ['.', ',']
greek = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu',
         'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
def removePunct(string):
    newstring = ''
    for ch in string:
        if ch in badpuncts:
            continue
        else:
            newstring += ch
    return newstring

words = removePunct(problem).split()
objects = open("objects.txt", "r+")
relations = open("relations.txt", "r+")

allObjects = objects.readlines()
allRelations = relations.readlines()
Objects = []
Relations = []
explicit = []
absObj = []
absRel = []

for obj in allObjects:
    newobj = obj.strip()
    if newobj:
        Objects.append(newobj)
for rel in allRelations:
    newrel = rel.strip()
    if newrel:
        Relations.append(newrel)

for wd in words:
    if wd.isupper():
        explicit.append(wd)
    elif wd.lower() in greek:
        explicit.append(wd)
    if wd.find('_') != -1:
        if wd[:wd.find('_')].lower() in greek:
            explicit.append(wd)
    else:
        for obj in Objects:
            if wd.find(obj) != -1:
                absObj.append(wd)
        for rel in Relations:
            if wd.find(rel) != -1:
                absRel.append(wd)

print(explicit)
print(absObj)
print(absRel)