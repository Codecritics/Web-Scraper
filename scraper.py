from requests import get

if __name__ == '__main__':
    print("Input the URL:")
    url = input()
    r = get(url)

    if str(r.status_code).startswith('3') or str(r.status_code).startswith('4') or str(r.status_code).startswith('5'):
        print(f"The URL returned {r.status_code}!")
    else:
        page_content = r.content
        with open('source.html', 'wb') as file:
            file.write(page_content)
        print("Content saved.")
