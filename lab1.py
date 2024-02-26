import requests

url = 'https://google.com/'

#url = input()

response = requests.get(url)

print(response.headers)


try: print(response.headers['Server'])
except: print('No server info present')

try: print(response.headers['Set-Cookie'])
except: print('No cookies present') 