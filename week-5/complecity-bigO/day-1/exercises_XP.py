#exercise-1
#   Snippet-1
#       O(n)
#   Snippet-2
#       O(n^2)
#   Snippet-3
#       O(logn)

#exercise-2
# numbers = [5, 2, 9, 1, 5, 6]
# def insertion_sort(numbers: list):
#     for i in range(1, len(numbers)):
#         value = numbers[i]
#         j = i - 1
#         while value < numbers[j] and j >= 0:
#             numbers[j + 1] = numbers[j] 
#             j -= 1 
#         numbers[j + 1] = value
# insertion_sort(numbers)


#exercise_3

# def find_number(numbers: list, num: int):
#     low = 0
#     high = len(numbers) - 1
#     while low <= high:
#         mid = (high + low) // 2
#         if numbers[mid] < num:
#             low = mid + 1
#         elif numbers[mid] > num:
#             high = mid - 1
#         elif numbers[mid] == num:
#             return mid
#     return False

# numbers = [1, 3, 5, 7, 9, 11]
# num = 2
# result = find_number(numbers, num)
# if result == True:
#     print(f"Element {num} found at index {result}")
# else:
#     print(f"Element {num} not found in the array")

# def isbalence(expr):
#     stack = []
#     open_pare = '({['
#     close_pare = ')}]'
#     for x in expr:
#         if x in open_pare:
#             stack.append(x)
#         elif x in close_pare:
#             if not stack or open_pare.index(stack.pop()) != close_pare.index(x):
#                 return False
#     return True


# expr = '(1 + 2) * [(3 / 4) - 5]}'
# if isbalence(expr):
#     print(f"The expression '{expr}' has balanced parentheses.")
# else:
#     print(f"The expression '{expr}' does not have balanced parentheses.")