import datetime
from pprint import pprint

from requests import get, delete, post

pprint(get('http://localhost:5000/api/v2/jobs').json())  # получение всех работ

pprint(post('http://localhost:5000/api/v2/jobs', json={'team_leader': 1, 'creater': 'Scott Ridley',
                                                       'job': 'test work abdsabasdbasqw',
                                                       'work_size': 52, 'collaborators': 2,
                                                       'start_date': str(datetime.date.today()),
                                                       'end_date': None,
                                                       'is_finished': None}).json())  # добавление работы

pprint(get('http://localhost:5000/api/v2/jobs/1').json())  # получение одной работы
pprint(get('http://localhost:5000/api/v2/jobs/999').json())  # получение одной работы (ошибка)

pprint(delete('http://localhost:5000/api/v2/jobs/7').json())  # удаление одной работы
pprint(delete('http://localhost:5000/api/v2/jobs/7').json())  # удаление одной работы (ошибка)
