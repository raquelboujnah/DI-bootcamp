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
