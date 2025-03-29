import datetime
from pprint import pprint

from requests import get, delete, post

# pprint(get('http://localhost:5000/api/v2/users').json())  # получение всех колонистов
#
# pprint(post('http://localhost:5000/api/v2/users',
#             json={'name': 'ABCD', 'surname': 'XYZ', 'age': 24, 'position': 'CAPTAIN', 'speciality': 'collector',
#                   'address': 'module_2', 'password': 123, 'password_again': 123,
#                   'email': 'collector@mars.org'}).json())  # добавление колониста
# pprint(post('http://localhost:5000/api/v2/users',
#             json={'name': 'ABC', 'surname': 'XY', 'age': 24, 'position': 'CAPTAIN', 'speciality': 'collector',
#                   'address': 'module_2', 'password': 123, 'password_again': 1234,
#                   'email': 'collector@mars.org'}).json())  # добавление колониста (ошибка)
# pprint(post('http://localhost:5000/api/v2/users',
#             json={'name': 'ABCD', 'surname': 'XYZ', 'age': 24, 'position': 'CAPTAIN', 'speciality': 'collector',
#                   'address': 'module_2', 'password': 123, 'password_again': 123,
#                   'email': 'collector@mars.org'}).json())  # добавление колониста (ошибка)
#
#
# pprint(get('http://localhost:5000/api/v2/users/1').json())  # получение одного колониста
# pprint(get('http://localhost:5000/api/v2/users/999').json())  # получение одного колониста (ошибка)
#
# pprint(delete('http://localhost:5000/api/v2/users/5').json())  # удаление одного колониста
# pprint(delete('http://localhost:5000/api/v2/users/5').json())  # удаление одного колониста (ошибка)

pprint(post('http://localhost:5000/api/v2/jobs', json={'team_leader': 1, 'creater': 'Scott Ridley',
                                                       'job': 'test work abdsabasdbasqw',
                                                       'work_size': 52, 'collaborators': 2,
                                                       'start_date': str(datetime.date.today()),
                                                       'end_date': None, 'is_finished': None}).json())
