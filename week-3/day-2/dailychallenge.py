import math
class Pagination:
    
    def __init__(self, items, page_size = 10):
        self.items = items
        self.page_size = int(page_size)
        self.current_page = 1
        self.total_page = math.ceil((len(self.items)/self.page_size))
        
    def get_visible_item(self):
        visible_item = self.items[self.current_page * self.page_size : self.current_page * self.page_size + self.page_size]
        print(visible_item)
            
    def firstPage(self):
        self.current_page = 0
        return self
    
    def lastPage(self):
        self.current_page = self.total_page
        return self

    def goToPage(self, pageNum):
        if pageNum <= self.total_page and pageNum > 0:
           self.current_page = pageNum
        else:
            print("wrong page")
        return self
        
    def nextPage(self):
        if self.current_page < self.total_page:
           self.current_page += 1
        elif self.current_page == self.total_page:
           self.current_page = 1
        return self
    
    def prevPage(self):
        if self.current_page > 1:
            self.current_page -= 1
        else:
            self.current_page = self.total_page
        return self
    

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
p.get_visible_item()
p.nextPage()
p.get_visible_item()
p.lastPage()
p.get_visible_item()
p.firstPage()
p.get_visible_item()

