from pprint import pprint

from requests import get, delete

print(delete('http://localhost:5000/api/jobs/12123').json())
print(delete('http://localhost:5000/api/jobs/asddsad').json())
print(delete('http://localhost:5000/api/jobs/').json())
print(delete('http://localhost:5000/api/jobs/6').json())

# получение всех работ
pprint(get('http://localhost:5000/api/jobs').json())
