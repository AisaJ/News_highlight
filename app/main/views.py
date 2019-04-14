from flask import render_template
from . import main
from ..requests import get_news,get_article

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


@main.route('/article/<title>')
def article():
  '''
  View article page function that returns the articles' details
  '''
  article = get_article(id)
  title = f'{article.title}'
  
  return render_template('article.html',title = title, article = article)
  
  