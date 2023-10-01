#exercise-1
def first_and_last(numbers: list):
    sum = numbers[0] + numbers[-1]
    return sum

#O(1)

#exercise-2
# def duplicates_count(numbers: list):
#     duplicate_num = []
#     duplicate_count = 0
#     for x in numbers:
#         if x in duplicate_num: 
#             duplicate_count += 1  
#         else:
#             duplicate_num.append(x)
#     return duplicate_count

# print(duplicates_count([2, 2, 2, 5, 7, 9, 9]))
#O(n)
#no because we have to do a loop

#exercise-3
# def pair_sum_zero(numbers: list):
#     pairs = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] == 0:
#                 pairs.append((numbers[i], numbers[j]))
#     return pairs

# print(pair_sum_zero([-2, 1, 2, 7, -7, -1, 8]))

#O(n^2)


            
