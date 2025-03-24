from pprint import pprint

from requests import get

# получение всех работ
pprint(get('http://localhost:5000/api/v2/users').json())
