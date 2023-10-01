# #exercise-1
# def insert_to_list():
#     list_num = [1, 3, 4, 5]
#     list_num.insert(1, 2)
#     print(list_num)

# insert_to_list()

# #exercise-2 
# def count_spaces():
#     spaces = 0
#     the_string = 'la vie est belle comme moi'
#     for x in the_string:
#         if x == " ":
#             spaces += 1
#     return spaces
# print(count_spaces())

# #exercise-3
# def count_upper_lower():
#     upper = 0
#     lower = 0
#     the_string = 'La Vie est Belle comme moi'
#     for x in the_string:
#         if x.isalpha():
#             if x.islower():
#                 lower += 1
#             elif x.isupper():
#                 upper += 1   
#     return f"number of upper letter: {upper}, number of lower letter: {lower}"

# print(count_upper_lower())

# #exercise-4
# def sum_list():
#     list_num = [1, 3, 4, 5]
#     list_sum = 0
#     for num in list_num:
#         list_sum += num
#     return list_sum

# print(sum_list())

# #exercise-5
# def find_max():
#     list_num = [0,1,3,50]
#     return max(list_num)

# print(find_max())

# #exercise-6
# def factorial(number):
#     result = 1
#     for i in range(2, number + 1):
#         result *= i
#     return result

# print(factorial(5))
    
# #exercise-7
# def count_item():
#     list_item = (['a','a','t','o'],'a')
#     count = 0
#     for x in list_item:
#         count += 1
#     return count
# print(count_item())

# #exercise-8
# import math
# def get_l2_norm():
#     norm = [1,2,2]
#     sum_of_squares = sum(x ** 2 for x in norm)
#     result = math.sqrt(sum_of_squares)
#     return result

# print(get_l2_norm())

#exercise-9
# def is_monotonic():
#     list_num = [7, 6, 5, 5, 2, 0]
#     is_asc = is_desc = True
#     for i in range(1, len(list_num)):
#         if list_num[i] < list_num[i - 1]:
#             is_asc = False
#             break

#     for i in range(1, len(list_num)):
#         if list_num[i] > list_num[i - 1]:
#             is_desc = False
#             break
        
#     return is_asc or is_desc

# print(is_monotonic())

# #exercise-10
# def longuest_word():
#     list_word = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'rush', 'south']
#     return max(list_word, key=len)

# print(longuest_word())

#exercise-11
# def int_and_string():
#     list_1 = ['correction', 1, 'childish', 2, 'beach', 'python', 4, 9, 'assertive']
#     int_item = []
#     str_item = []
#     for x in list_1:
#         if isinstance(x, int):
#             int_item.append(x)
#         if isinstance(x, str):
#             str_item.append(x)
#     return f"{int_item}, {str_item}"

# print(int_and_string())

# #exercise-12
# def is_palidrone():
#     word = 'radar'
#     word_reverse = word[::-1]
#     if word == word_reverse:
#         return True
#     else:
#         return False
        
# print(is_palidrone())
            
# #exercise-13
# def get_length():
#     sentence = 'Do or do not there is no try'
#     k = 2
#     list_word = sentence.split()
#     count = 0
#     for word in list_word:
#         if len(word) > k:
#             count += 1
#     return count

# print(get_length())

# #exercise-14
# def get_average():
#     dict_avg = {'a': 1,'b':2,'c':8,'d': 1}
#     sum_value = sum(dict_avg.values())
#     average = sum_value / len(dict_avg)
#     return average

# print(get_average())

# #exercise-16
# def is_prime():
#     num = 11
#     for i in range(3, num + 1, 2):
#         if num % i == 0:
#             return True
        
# print(is_prime())

# #exercise-17
# def value_index_iseven():
#     weird_print = [1,2,2,3,4,5]
#     even_list = []
#     for i, value in enumerate(weird_print):
#         if i % 2 == 0 and value % 2 == 0:
#             even_list.append(value)
#     return even_list

# print(value_index_iseven())

# #exercise-18
# def count_types(**kwargs):
#     type_counts = {}

#     for value in kwargs.values():
#         value_type = type(value)
#         type_counts[value_type] = type_counts.get(value_type, 0) + 1

#     return type_counts
            
# print(count_types(a=1,b='string',c=1.0,d=True,e=False))

# #exercise-19
# def split_simlulation(split):
#     string = 'la vie est belle comme moi'
#     for x in string:
#         if x == split:
#             x.replace(",", split)
#     return string

# print(split_simlulation(" "))

# #exercise-20
# def password(secret):
#     password_secret = "*" * len(secret)
#     return password_secret

# print(password('boujnah22'))
        
