## create a new list that only contains the uppercased words


words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
capital_word = []

for capital in words:
    if capital.isupper():
        capital_word.append(capital)
        
print(capital_word)



bank_accout = 10000
computer_price = 2000
count = 0 

while bank_accout >= computer_price:
    print("i buy a computer")
    bank_accout -= computer_price
    count += 1
    
print(f"i have {bank_accout} dollars left and i bought {count} computers")


    