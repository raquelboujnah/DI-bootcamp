from anagram_checker import AnagramChecker
 
def show_menu():
    print("Welcome to our anagram checker!")
    user_word = input("Type a word of your choice to find his anagram. If you want to quit this anagram checker typr 'quit'")
    print(user_word)
    return user_word

def analize_input(user_word):
    list_word = user_word.split(" ")
    list_word.replace(" ", "")
    if len(list_word) > 1:
        raise Exception(input("Error type only one word please"))#is this ok?
    else:
        if user_input.isalpha():
            return True
    
def main(user_word):
    wrd = AnagramChecker("text_file.txt")
    show_menu()
    analize_input(user_word)  
    if analize_input() == True:
        wrd.is_valid(user_word)
        if wrd.is_valid == True:
            wrd.get_anagrams(user_word)
            print(f"Your word: {user_word}\nThis is a valid word is English\nAnagram for your word:{' '.join(wrd.get_anagrams())}")
        else:
            print("you word is not in English")
            show_menu()
    else:
        print("Your word is not valid")
        show_menu() 
        
user_input = show_menu()
main(user_input)