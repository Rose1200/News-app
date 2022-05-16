
from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Current Affairs'
    data = get_news()

    return render_template("index.html", title=title, articles=data)



