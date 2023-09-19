import itertools
class AnagramChecker:
    
    def __init__(self, text_file):
        with open(text_file, "r") as word_file:
            read = word_file.read()
            self.text = read.split()
            
    def is_valid(self, word):
        word = word.upper()
        if word in self.text:
            return True
        else: 
            return False
        
    def get_anagrams(self, word):
        permutations = [''.join(p) for p in itertools.permutations(word)]
        anagrams = [perm for perm in permutations if perm != word]
        list_anagram = []
        for option in anagrams:
            if option in self.text:
                list_anagram.append(option)
        return list_anagram

wrd = AnagramChecker("text_file.txt")
print(wrd.get_anagrams("team"))



