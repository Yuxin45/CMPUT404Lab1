import requests
print(requests.__version__)


r = requests.get('http://google.com/', auth=('user', 'pass'))
print(r.status_code)