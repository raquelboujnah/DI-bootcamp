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