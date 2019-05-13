import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


NET_LOC = 'www.bbc.com'


def parse_bbc(chapters: str, num: int):
    try:
        resp = requests.get(f'https://{NET_LOC}/{chapters}')
        resp.raise_for_status()

        soup = BeautifulSoup(resp.content.decode(), 'html.parser')
    except Exception:
        return None

    res = []
    for link in soup.find_all('h3'):
        if len(res) == num:
            break

        try:
            text = link.string
            parse_link = urlparse(link.parent.get('href'))
            if not parse_link.netloc:
                parse_link = parse_link._replace(netloc=NET_LOC)._replace(scheme='https')
        except Exception:
            pass
        else:
            res.append((text, parse_link.geturl()))

    return res


if __name__ == '__main__':
    from pprint import pprint
    pprint(parse_bbc('sport', 10))
