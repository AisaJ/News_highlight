from flask import render_template
from . import main

#view functions
@main.route('/')
def index():
  '''
  View the root page 
  '''
  news_headlines = get_news('top-headlines')
  print(news_headlines)
  title = 'Catch the latest and breaking news world wide'
  return render_template('index.html',title = title, headlines= news_headlines)


@main.route('/sources/<>')
def source():
  '''
  View news pages function that returns the news articles available
  '''
  
  return render_template('source.html')