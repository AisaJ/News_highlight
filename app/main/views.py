from flask import render_template
from . import main

#view functions
@main.route('/')
def index():
  '''
  View the root page 
  '''
  return render_template('index.html')


@main.route('/sources/<>')
def source():
  '''
  View news pages function that returns the news articles available
  '''
  return render_template('source.html')