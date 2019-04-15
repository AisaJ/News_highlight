class News:
  '''
  News class to define News objects
  '''
  def __init__(self,id,name,description,url,category,country):
    
    self.author = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.country = country
