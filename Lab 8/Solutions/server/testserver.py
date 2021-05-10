import requests

r = requests.post('http://127.0.0.1:5000/register',params={'id':'iandonlyi'})
print(r)
r = requests.post('http://127.0.0.1:5000/register',params={'id':'someofyou'})
print(r)
r = requests.post('http://127.0.0.1:5000/send',json={'from':'someofyou','to':'iandonlyi','message':'hello there'})
print(r)
r = requests.post('http://127.0.0.1:5000/send',json={'from':'iandonlyi','to':'someofyou','message':'general kenobi'})
print(r)
r = requests.get('http://127.0.0.1:5000/receive',params={'id':'iandonlyi'})
print(r)
print(r.json())
r = requests.get('http://127.0.0.1:5000/receive',params={'id':'someofyou'})
print(r)
print(r.json())