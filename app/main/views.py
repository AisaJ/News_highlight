from flask import render_template
from . import main

#view functions
@main.route('/')
def index():
  '''
  View the root page 
  '''
  return render_template('index.html')