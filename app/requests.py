import urllib.request,json
from .models import News,Articles

#Getting api key
apiKey = None

#Getting the news base url
base_url = None

#Getting sources base url
src_base_url = None

def configure_request(app):
  global apiKey,base_url, src_base_url
  apiKey = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']
  src_base_url = app.config['SOURCE_API_BASE_URL']

def get_news():
  '''
  Function that gets the json response to our url request
  '''
  get_news_url = base_url.format(apiKey)

  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_sources = None

    if get_news_response['sources']:
        news_sources_list = get_news_response['sources']
        news_sources= process_sources(news_sources_list)

  return news_sources


def process_sources(news_list):
  '''
  Function that processes the news sources to list of objects
  '''
  news_sources = []
  for news_item in news_list:
    id =  news_item.get('id')
    name = news_item.get('name')
    description = news_item.get('description')
    url = news_item.get('url')
    category = news_item.get('category')
    language = news_item.get('language')

  
    news_object = News(id,name,description,url,category,language)
    news_sources.append(news_object)

  return news_sources

def get_source(id):
  get_source_details_url = src_base_url.format(id,apiKey)

  with urllib.request.urlopen(get_source_details_url) as url:
    source_details_data = url.read()
    source_details_response = json.loads(source_details_data)

    articles_results = None

    if source_details_response['articles']:
      articles_list = source_details_response['articles']
      articles_results = process_articles(articles_list)

  return articles_results
  
def process_articles(articles_list):
  '''
  Function that processes the articles to objects
  '''
  articles_results = []
  for article_item in articles_list:
    id = article_item.get('id')
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    image = article_item.get('urlToImage')
    date = article_item.get('date')
    content = article_item.get('content')

    if image:
      article_object = Articles (id,author,title,description,image,date, content)
      articles_results.append(article_object)
  return articles_results



