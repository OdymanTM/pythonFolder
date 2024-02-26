import requests

url = 'https://instagram.com/'

url = input('Insert url:')
if not url.startswith('https://'):
    url = 'https://' + url

with requests.get(url) as response:
    print('Headers are:' , response.headers)

    try: print(response.headers['Server'])
    except: print('No server info present')

    cookies = response.headers.get('Set-Cookie')
    #dioti mporei na einai polla to ekana me auton ton tropo
    if cookies:
        print('These are the cookies found: ',cookies)
    else:
        print('No cookies present')