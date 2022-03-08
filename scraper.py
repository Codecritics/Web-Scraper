from requests import get
from json import loads

if __name__ == '__main__':
    print("Input the URL:Input the URL:")
    url = input()

    response_url = get(url)
    if str(response_url.status_code).startswith('4'):
        print("Invalid quote resource!")
    else:
        content = loads(response_url.text)
        try:
            print(content['content'])
        except KeyError:
            print("Invalid quote resource!")
