class News:
  '''
  News class to define News objects
  '''
  def __init__(self,id,name,description,url,category,language):
    
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language


class Articles:
  '''
  Articles class for defining Articles objects
  '''
  def __init__(self,id, author,title,description,image,date,content,url):
    self.id = id
    self.author = author
    self.title = title
    self.description = description
    self.image = image
    self.date = date
    self.content = content
    self.url = url
