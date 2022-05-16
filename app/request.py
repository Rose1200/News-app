# import urllib3.request
import requests
from app import app
from .models.news import News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting news base url
base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    response = requests.get(get_news_url).json()
    
    return response['articles']


#     with urllib3.request.urlopen(get_news_url) as url:
#         get_news_data = url.read()
#         get_news_response = json.loads(get_news_data)

#         news_results = None

#         if get_news_response['articles']:
#             news_results_list = get_news_response['articles']
#         #  print result list
#         news_results = process_results(news_results_list)

#     return news_results

# def process_results(news_list):
#     '''
#     Function that processes news results and transforms it to a list of objects
#     '''
#     news_results = []
#     for news_items in news_list:
#         author = news_items.get('author')
#         title = news_items.get('title')
#         description = news_items.get('description')
#         urlToImage = news_items.get('urlToImage')
#         content = news_items.get('content')
#         publishedAt = news_items.get('publishedAt')

#         news_object = News(author,title,description,urlToImage,content,publishedAt)
#         # print(news_object)
#         news_results.append(news_object)
#         # print(news_results)

#     return news_results
