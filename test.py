from pprint import pprint

from requests import post, get

# пустой запрос
print(post('http://localhost:5000/api/jobs', json={}).json())

# неполный запрос
print(post('http://localhost:5000/api/jobs',
           json={'title': 'Заголовок'}).json())

# корректный запрос
print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'creater': 'Scott Ridley',
                 'job': 'black work',
                 'work_size': 200,
                 'collaborators': '2,3,4',
                 'start_date': None,
                 'end_date': None,
                 'is_finished': False}).json())

# получение всех работ
pprint(get('http://localhost:5000/api/jobs').json())
