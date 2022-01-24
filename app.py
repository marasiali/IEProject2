from unittest import result
from flask import Flask
from flask import render_template
from flask import make_response
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html', query=None, page=None, results=None)

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    query = args.get('query')
    page = args.get('page')
    results = get_links(query, page)
    return render_template('index.html', query=query, page=page, results=results)

def get_links(query, page):
    return [
        {'link': 'https://jinja.palletsprojects.com/en/3.0.x/templates/', 
        'caption': 'www.giksy.com/fdsgngkdsbjfbjdssdgdsg', 
        'title': 'This is our site please visit us!', 
        'description':"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        }, 
        {'link': 'https://jinja.palletsprojects.com/en/3.0.x/templates/', 
        'caption': 'www.giksy.com/fdsgngkdsbjfbjdssdgdsg', 
        'title': 'This is our site please visit us!', 
        'description':"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        },
        {'link': 'https://jinja.palletsprojects.com/en/3.0.x/templates/', 
        'caption': 'www.giksy.com/fdsgngkdsbjfbjdssdgdsg', 
        'title': 'This is our site please visit us!', 
        'description':"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        }
    ]