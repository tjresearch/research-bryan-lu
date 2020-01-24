import requests
r = requests.post('http://localhost:9000/?properties={"annotators":"tokenize,ssplit,pos,depparse,parse,ner,natlog,sentiment","outputFormat":"json",'
                  '"data":"In circle O, diameter AB is perpendicular to chord CD at E"}')
data = r.json()
for k, v in data.items():
    print(str(k) + str(v))
#params = {'properties' : {"annotators" : "tokenize,ssplit,pos", 'outputFormat' : 'json'}, 'data' : "In circle O, diameter AB is perpendicular to chord CD at E"}
#print(requests.post('http://localhost:9000'), data=params)
