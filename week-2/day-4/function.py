#1. create a function that takes a number as an argument, and check if this number is even or odd
#2. create a function that takes a list of numbers as an argument, and check if each number is even or odd

# def odd_even (num):
#     if num % 2 == 0:
#        print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
        
# odd_even(22)
# odd_even(33)
# odd_even(5)

# def list_num (numbers):
#     for x in numbers:
#         if x % 2 == 0:
#             print(f"{x} is even")
#         else:
#             print(f"{x} is odd")
            
# list_num([22, 44, 6, 77, 54])


#exercise

# 1st function - get_price_car
# receive the age of the user 
# and if the user is > 40
#     --> 200
# if the user is < 40
#     --> 300

def get_price_car ():
    user_age = int(input("what is your age"))
    if user_age > 40 :
        return 200
    else : 
        return 300


# 2nd function - get_price_flight
# receive a destination from the user
# if the destinatation is Paris
#     --> 400
# if not
#     --> 600

def get_price_flight ():
    user_destination = input("choose a destination")
    if user_destination == "paris".lower():
        return 400
    else:
        return 600
    
# 3rd function
# is going to use the result from the 2 functions above
# and inform the user of the total price of the vacation
def inform_vacation_price ():
    total = get_price_car() + get_price_flight()
    return total

print(f"your total vacation price is {inform_vacation_price()}")
    
 # def check_answers () :##we create a function
#     number_correct_answers = 0 ##we create a variable who will accept only good answer
#     number_incorrect_answers = 0 ##we create a variable who will accept only wrong answer
#     list_wrong_answers = [] ##we create an empty list who will crate a list of dictionarys of wrong answer with the question an the right asnwer

#     print("\n ---- The quizz starts ----")##inform the user that the quizz starts
#     for quizz in star_wars : ##we open a loop that will go insinde the data and print question by question
#         user_answer = input(quizz["question"]) ##we print the question with an input to let the user add his answer
#         if user_answer.lower() == quizz["answer"].lower():##we check the answer of the user 
#              number_correct_answers += 1##if the users answer is the same of the actual answer then we add 1 to the number_correct_answer
#         else : ##if the answer is not the same of the actual answer:
#             number_incorrect_answers += 1##then we add 1 to the number_incorrect_answer
#             new_quizz = quizz.copy() ##make a copy of the dictionary that we are actualy in 
#             new_quizz["user_answer"] = user_answer## and we add a new key called user_answer with is answer
#             list_wrong_answers.append(new_quizz)##now we add the dictonary we just copy with the new key and we add it to list_wrong_answer
    
#     inform_user(number_correct_answers, number_incorrect_answers, list_wrong_answers)##here we call the next function so the code could run again if we play again and we add it all the variable we need for run the code

# def inform_user (correct, incorrect, wrong_answers) :##here we create the new function and we gave a name to each argument for us to be easyier
#     print("\n ----------------------------")##just to separate the quizz to his results
#     print(f"You have {correct} correct answers")##we inform the user of his correct answer by using his parametter
#     print(f"You have {incorrect} incorrect answers")##we inform the user of his incorrect answer by using his parametter
#     for global_answer in wrong_answers :##we open a loop to go in each dictionary in the list we creat: list_wrong_answer that is now called wrong_answer
#         print(f'The question was {global_answer["question"]}')##we print the question of the dictionary
#         print(f'Your answer was {global_answer["user_answer"]}')##we print the user's answer of the dictionary
#         print(f'Your got it wrong, the correct answer is {global_answer["answer"]}')##and we print the right answer
    
#     print("\n --------------------")
#     if incorrect > 3 :##if the number of incorrect answer is bigger than 3 
#         print(" YOU GOT MORE 3 ANSWERS WRONG Play Again")##so we inform the user to try again
#         check_answers()##we call the first function to run the quiz again
#     else :##if not
#         print("Good Job - YOU DONT NEED TO REDO THE GAME")##we print good job

# check_answers()##we call the first function for all the code to run 
    