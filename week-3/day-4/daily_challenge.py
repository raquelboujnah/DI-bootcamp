class Text:
    
    def __init__(self, text):
        self.text = text.split()
        
    def frequency(self, word):
        print(f"the word {word} is present {self.text.count(word)} time in the text")  
        
    def most_frequent(self):
        counter = 0
        word = self.text[0]
        for i in self.text:
            curr_frequency = self.text.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                word = i
        return word
    
    def unique_word(self):
        unique = set(self.text)
        return unique
    
    @classmethod
    def file_text(cls, file_name):
        with open(file_name , "r") as file:
            read_file = file.read()
            return cls(read_file)
        
text_word = "A good book would sometimes cost as much as a good house."
txt2 = Text.file_text("stranger.txt")
txt = Text(text_word)
txt.frequency("good")
print(txt.most_frequent())
print(txt.unique_word())
print(txt2.most_frequent())



