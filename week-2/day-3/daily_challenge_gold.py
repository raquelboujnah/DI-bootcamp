user_choice = input("would you like to encryption or decryption?\n")
user_msg = input('enter your msg:\n')
if user_choice == "encryption":
    cypher_text_encr = ""
    for letter in user_msg:
        cypher_text_encr += chr(ord(letter) + 3)
    cypher_text = cypher_text_encr.replace('#', ' ')
    print(cypher_text)
    
elif user_choice == 'decryption':
    cypher_text_decr = ""
    for letter in user_msg:
        cypher_text_decr += chr(ord(letter) - 3)
    print(cypher_text_decr)
    
elif user_choice not in "encryption" or "decryption":
    print("didnt understand what yo want to do")