from flask import render_template
from . import main
from ..requests import get_news,get_source

#view functions
@main.route('/')
def index():
  '''
  View the root page 
  '''
  sources = get_news()
  # news_headlines = get_news('headlines')
  # print(news_headlines)
  # breaking_news = get_news('breakingNews')
  # print(breaking_news)
  # title = 'Catch the latest and breaking news world wide'
  return render_template('index.html',sources = sources)


@main.route('/source/<id>')
def source(id):
  '''
  View article page function that returns the sources' details
  '''
  source = get_source(id)
  
  
  return render_template('source.html', articles_list = source)
  
  