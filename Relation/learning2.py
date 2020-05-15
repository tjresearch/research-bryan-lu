import nltk
import sklearn

testcases = open("finaltestcases.py", "r+")
numtestcases = 40
testproblems = []
testlines = testcases.readlines()

for i in range(numtestcases):
    problem = testlines[2*i]
    correctrels = testlines[2*i+1]
    goodrelslist = correctrels.split("%")  # format test cases with this
    problemTup = (problem, goodrelslist)
    testproblems.append(problemTup)

