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
  get_source_details_url = base_url.format(id,apiKey)

  with urllib.request.urlopen(get_source_details_url) as url:
    source_details_data = url.open()
    source_details_response = json.loads(source_details_data)

    news_object = None
    if source_details_response:
      id = source_details_response.get('id')
      name = source_details_response.get('name')
      description = source_details_response.get('description')
      url = source_details_response.get('url')
      category = source_details_response.get('categry')
      language = source_details_response.get('language')

      news_object = Sources(id,name,description,url,category,language)

  return news_object
