import urllib.request,json
from .models import News

#Getting api key
apiKey = None

#Getting the news base url
base_url = None

def configure_request(app):
  global apiKey,base_url
  apiKey = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
  '''
  Function that gets the json response to our url request
  '''
  get_news_url = base_url.format(category,apiKey)

  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_articles = None

    if get_news_response['articles']:
        news_articles_list = get_news_response['articles']
        news_articles = process_articles(news_articles_list)

  return news_articles


def process_articles(news_list):
  '''
  Function thaat processes the news articles to list of objects
  '''
  news_articles = []
  for news_item in news_list:
    title =  news_item.get('title')
    author = news_item.get('author')
    description = news_item.get('description')
    image = news_item.get('urlToImage')
    date = news_item.get('publishedAt')
    content = news_item.get('content')

    if image:
      news_object = News(title,author,description,image,date,content)
      news_articles.append(news_object)

  return news_articles

def get_article(title):
  get_article_details_url = base_url.format(title,apiKey)

  with urllib.request.urlopen(get_article_details_url) as url:
    article_details_data = url.open()
    article_details_response = json.loads(article_details_data)

    news_object = None
    if article_details_response:
      title = article_details_response.get('title')
      author = article_details_response.get('author')
      description = article_details_response.get('description')
      image = article_details_response.get('urlToImage')
      date = article_details_response.get('publishedAt')
      content = article_details_response.get('content')

      news_object = Article(title,author,description,image,date,content)

  return news_object
