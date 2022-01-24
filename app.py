from flask import Flask
from flask import render_template
from flask import request
from scraper import google_search, yahoo_search

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html', query=None, page=None, results=None)


@app.route('/search', methods=['GET'])
def search():
    args = request.args
    query = args.get('query')
    page = int(args.get('page', 1))
    print(page)
    results = get_links(query, page)
    return render_template('index.html', query=query, page=page, results=results)


def get_links(query, page):
    google_results = google_search(query, page)
    yahoo_results = yahoo_search(query, page)
    results = {}
    for i, item in enumerate(google_results):
        item['google_index'] = i
        item['yahoo_index'] = None
        results[item['link']] = item
    for i, item in enumerate(yahoo_results):
        if item['link'] in results:
            results[item['link']]['yahoo_index'] = i
        else:
            item['google_index'] = None
            item['yahoo_index'] = i
            results[item['link']] = item
    return sorted(results.values(), key=get_item_score, reverse=True)

def get_item_score(item):
    score = 0
    if item['google_index'] is not None:
        score += 60 * (1 / (item['google_index'] + 1))
    if item['yahoo_index'] is not None:
        score += 15 * (1 / (item['yahoo_index'] + 1))
    return score

