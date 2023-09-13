class Text:
    
    def __init__(self, text):
        self.text = text.split()
        
    def frequency(self, word):
        word_list = self.text
        print(f"the word {word} is present {word_list.count(word)} time in the text")  
        
    def most_frequent(self):
        word_list = self.text
        counter = 0
        num = word_list[0]
        for i in word_list:
            curr_frequency = word_list.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = i
        return num
    
    def unique_word(self):
        word_list = self.text
        unique = set(word_list)
        return unique
    
    @classmethod
    def file_text(cls, file_name):
        with open(file_name , "r") as file:
            read_file = file.read()
            return Text(read_file)
        
text_word = "A good book would sometimes cost as much as a good house."
txt2 = Text.file_text("stranger.txt")
txt = Text(text_word)
txt.frequency("good")
print(txt.most_frequent())
print(txt.unique_word())
print(txt2.most_frequent())



