import requests
from bs4 import BeautifulSoup
import sys


def usage() -> None:
    print("usage: search.py [search term]")
    print("example: search.py \"Hello World\"")
    exit(1)


if len(sys.argv) != 2:
    usage()


term = sys.argv[1]


HEDAERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
}


def search(start=0) -> None:

    url = f'https://www.google.com/search?q={term}'

    if start > 0:
        url += f"&start={start}"

    r = requests.get(url, headers=HEDAERS)

    soup = BeautifulSoup(r.text, 'html.parser')

    divs = soup.find_all('div', {'class': 'g'})

    for div in divs:
        heading = div.find_all('h3', {'class', "LC20lb DKV0Md"})
        body = div.find_all(
            'div', {'class', "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"})
        body2 = div.find_all(
            'div', {'class': 'lEBKkf'})
        timestamp = div.find_all('div', {'class': 'uo4vr'})
        link = div.find('a')

        print()
        if len(heading):
            print(heading[0].text)
        if len(body):
            print(body[0].text)
        if len(body2):
            print(body2[0].span.text)
        if len(timestamp):
            print(timestamp[0].text)
        print("url:", link["href"])
        print()

    if start == 0:
        print("No results found")

    if len(divs) == 0:
        return

    print("---More--- (q to quit)")
    if input().lower() == 'q':
        return
    search(start + 10)


search()
