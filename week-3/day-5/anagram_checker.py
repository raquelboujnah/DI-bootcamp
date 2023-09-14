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



#   word1 = [word[i] for i in range(0, len(word))]
#         word1 = sorted(word)
#         anagram_word = []
#         for words in self.text:
#             sort_words = sorted(words)
#             if word1 == sort_words:
#                 anagram_word.append(words)
#         print(anagram_word)
        
#  anagram_list = []
#         for words in self.text:
#             letter_list = []
#             for letter in words:
#                 if letter in word:
#                     letter_list.append(letter)
#             if len(letter_list) == len(word):
#                 anagram_list.append(words)
#         return anagram_list
                
