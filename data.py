import requests as rq

API_URL = 'https://opentdb.com/api.php?amount=10&type=boolean'

question_data = rq.get(API_URL).json()['results']
