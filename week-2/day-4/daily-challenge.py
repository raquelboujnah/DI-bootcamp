#     7ii
#     Tsx
#     h%?
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!

matrix = [
    ["7", "i", "i"],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i", " ", "#"],
    ["s","M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]
def exrtact(matrix):
    list1 = []
    column_list1 = [item[0] for item in matrix]
    if letter.isalpha() in column_list1:
        list1.append(letter)
    print(list1)
exrtact(matrix)

def sortir(matrix):
    list2 = []
    column_list2 = [item[1] for item in matrix]
    if letter.isalpha() in column_list2: 
        list2.append(letter)
    print(list2)

sortir(matrix)
    
def out(matrix):
    list3 =[]
    column_list3 = [item[2] for item in matrix]
    if letter.isalpha() in column_list3:
        list3.append(letter)
    print(list3)

out(matrix)
    
def join(matrix):
    the_secret = exrtact() + sortir() + out()
    print(f"the secret sentence inside the matrix is {the_secret}")

join(matrix)


secret = """7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!"""

def create_colums() :
    secret_list = list(secret.split("\n"))
    lst = []
    for num in range(3) :
        lst.append([char[num] for char in secret_list])

    return lst

def decode() :
    secret = create_colums()
    # print("secret list", secret)
    final = ""
    for arr in secret :
        for char in arr :
            if str(char).isalpha() :
                    final += char
            else :
                final += " "
    print(final)

decode()
    