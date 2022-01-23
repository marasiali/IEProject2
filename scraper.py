import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build


GOOGLE_API_KEY = 'AIzaSyA_BlmjhsPfrQ0d8sT0ZEZxCF4DWY-xzro'
GOOGLE_SEARCH_ENGINE_ID = 'cc327526371294410'
service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)


def yahoo_search(text, page=1):
    first_item_index = (page - 1) * 7 + 1
    formatted_text = '+'.join(text.split())
    response = requests.get(f'https://search.yahoo.com/search?p={formatted_text}&b={first_item_index}')
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for item in soup.select('.algo'):
        title_box = item.select_one('a.td-hu')
        results.append({
            'title': title_box.contents[-1],
            'link': title_box['href'],
            'desc': item.select_one('.fc-falcon').text
        })
    return results


def google_search(text, page=1):
    first_item_index = (page - 1) * 10 + 1
    response_data = service.cse().list(
        q='test',
        cx=GOOGLE_SEARCH_ENGINE_ID,
        start=first_item_index
    ).execute()

    results = []
    for item in response_data['items']:
        results.append({
            'title': item['title'],
            'link': item['link'],
            'desc': item['snippet'],
        })
    return results
