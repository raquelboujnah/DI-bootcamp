class Pagination:
    
    def __init__(self, items, page_size = 10):
        self.items = items
        self.page_size = int(page_size)
        self.current_page = 0
        self.total_page = int(len(self.items)/4)
        
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
        self.current_page = pageNum
        return self
        
    def nextPage(self):
        self.current_page += 1
        return self
    
    def prevPage(self):
        self.current_page -= 1
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

