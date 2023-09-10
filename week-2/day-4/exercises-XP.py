import random
# #exercise-1
# def display_message():
#     print("we are learning about function in python")

# display_message()

# #exercise-2
# def favorite_book(title):
#     print("my familly favorite book is " + title)

# favorite_book("Harry Potter")

# #exercise-3
# def describe_city(city, contry = "isreal"):
#     print(city + " is in " + contry)

# describe_city("tel aviv")
              
#exercise-4
# def choose_number(user_number):
#     random_number = random.randint(1, 100)
#     if user_number == random_number:
#         return "its the same number" + random_number
#     else:
#         return f"its a fail {user_number}  {random_number}"


# user_input = int(input("choose a number between 1-100"))
# choose_number(user_input)


# #exercise-5
# def make_shirt(size = "large", text = "i love python") :
#     print("the size of the shirt is " + size + " and the message is " + text)

# make_shirt()
# make_shirt("medium")
# make_shirt("small", "python is cool")

#exercise-6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel'] 
# def show_magicians(magician_names):
#     for name in magician_names:
#         print(name)
        
# show_magicians(magician_names)

# def make_great(magician_names):
#     for name in range(len(magician_names)):
#       magician_names[name] = magician_names[name] + " The Great"
 
# make_great(magician_names)
# show_magicians(magician_names)

#exercise-7
# def get_random_temp():
#     season = int(input("in which month are we type a number between 1-12"))
#     if 1 <= season <= 4:
#        random_temp = round(random.uniform(-10, 16),2)
#     elif 5 <= season <= 7:
#         random_temp = round(random.uniform(17, 23),2) 
#     elif 8 <= season <= 10:
#          random_temp = round(random.uniform(24, 32),2)
#     elif 11 <= season <= 12:
#          random_temp = round(random.uniform(33, 40),2)
    
#     return random_temp

# def main():
#     temp = get_random_temp()
#     print(f"the temperature right now is {temp}")
#     if temp < 0:
#         print("Brrr, that's freezing! Wear some extra layers today")
#     elif 0 <= temp <= 16:
#         print("Quite chilly! Don't forget your coat")
#     elif 17 <= temp <= 23:
#         print("maybe bring a small jacket with just in case")
#     elif 24 <= temp <= 32:
#         print("the summer is here!!!")
#     else : 
#         print("better for you to stay at home today")

# main()

#exercise-8
star_wars = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

    
# def question_user(star_wars):
#     wrong_answer = 0
#     wrong_answer_list = []
#     for quiz in star_wars:
#         print(quiz["question"])
#         user_answer = input("what is your answer?\n")
#         if user_answer != quiz["answer"]:
#            wrong_answer += 1 
#            wrong_answer_list.append(quiz["question"])
#     print(wrong_answer_list)       
# question_user(star_wars)
 
# def quiz_result(star_wars):
#     for quest in wrong_answer_list:
#         print(f"in the question {quest} your answer was{user_answer} but the correct answer was {quiz["answer"]}")
#     if wrong_answer > 3:
#         print("you've done more that 3 mistakes try again to improve your knowleg in star wars")
#     print(f"you have done {wrong_answer} wrong answer")



 #THIS IS THE GOOD ONE👇🏻👇🏻  
   
def question_user():
    wrong_answer = 0
    good_answer = 0
    wrong_answer_list = []
    print("--------The quiz starts--------")
    for quiz in star_wars:
        print(quiz["question"])
        user_answer = input("what is your answer?\n")
        if user_answer != quiz["answer"]:
           wrong_answer += 1 
           new_quiz = quiz.copy()
           new_quiz["wrong_answer_user"] = user_answer
           wrong_answer_list.append(new_quiz)
        else:
            good_answer += 1
    
    quiz_result(wrong_answer, good_answer, wrong_answer_list) 


def quiz_result(wrong, good, list_):
    print("\n-----------------------")
    print(f"You have done {good} correct answer")
    print(f"You have done {wrong} wrong answer")
    for quest in list_:
        print(f"In the question {quest['question']} your answer was {quest['wrong_answer_user']} but the correct answer was {quest['answer']}")
        
    print("\n-----------------------")
    if wrong > 3:
        print("You've done more that 3 mistakes try again to improve your knowleg in star wars")
        question_user()
    else:
        print("Good job")

question_user()
      
      
        
