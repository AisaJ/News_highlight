from flask import render_template
from . import main
from ..requests import get_news

#view functions
@main.route('/')
def index():
  '''
  View the root page 
  '''
  news_headlines = get_news('headlines')
  print(news_headlines)
  breaking_news = get_news('breakingNews')
  print(breaking_news)
  title = 'Catch the latest and breaking news world wide'
  return render_template('index.html',title = title, headlines= news_headlines, breakingNews = breaking_news)


# @main.route('/sources/<>')
# def source():
#   '''
#   View news pages function that returns the news articles available
#   '''
  
#   return render_template('source.html')