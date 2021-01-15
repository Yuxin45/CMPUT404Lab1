import requests
print(requests.__version__)


r = requests.get('http://google.com/', auth=('user', 'pass'))
print(r.status_code)

githublink = requests.get("https://raw.githubusercontent.com/Yuxin45/CMPUT404Lab1/master/requestVersion.py")
print(githublink.text)