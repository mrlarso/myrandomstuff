import math

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page
      self.pages = self.get_pages()

  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)


  # returns the number of pages
  def page_count(self):
      return int(math.ceil(self.item_count()/float(self.items_per_page)))

  def get_pages(self):
      pages = []
      for page in range(0,self.page_count()):
          pages.append(self.collection[page*self.items_per_page:((page+1)*self.items_per_page)])
      return pages

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      if page_index >= len(self.pages) or page_index < 0:
          return -1
      return len(self.pages[page_index])

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if item_index >= len(self.collection) or item_index < 0 :
          return -1
      elif item_index == 0 and len(self.collection > 0):
          return 0
      else:
          return(int(math.ceil(float(item_index)/self.items_per_page))) - 1

p = PaginationHelper(['a','b','c','d','e','f'], 4)

print p.page_count()
print p.pages
for i in [0,1,2,-1]:
    print p.page_item_count(i)

for i in (0,1,5,8,-20):
    print p.page_index(i)
