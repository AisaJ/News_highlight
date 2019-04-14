import unittest
from app.models import News

class NewsTest(unittest.TestCase):

  def setUp(self):
    self.new_news = News('Rains','Michelle Tush','Expected rains in the month of April','https://images.unsplash.com/photo-1555089673-0b4b69c076d9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80','2019/03/12T06:40:00Z','Farmers get ready for the season')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
