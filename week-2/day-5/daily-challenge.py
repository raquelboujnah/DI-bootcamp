#challenge-1
def alphabet():
    user_sentence = list(sorted(input("Write a sentence that the words are only separated by comma: ").split(",")))
    print(",".join(user_sentence))
    
#alphabet()

#challenge-2
def find_longest():
    user_sentence = input("write a sentence: ")
    longest = max(user_sentence.split(" "), key=len)
    print(f"The longest word in your sentence is '{longest}'")
   
#find_longest()    