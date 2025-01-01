
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(orignal_text,shift_num):
    cipher_text=""
    for letter in orignal_text:
        position=alphabet.index(letter)
        new_position=(position+shift_num)
        new_position%=len(alphabet)
        cipher_text+=alphabet[new_position]
    print(f'Here is your encoded text is :{cipher_text}')


def decrypt(orignal_text, shift_num):
    cipher_text = ""
    for letter in orignal_text:
        position = alphabet.index(letter)
        new_position = (position - shift_num)
        new_position %= len(alphabet)
        cipher_text += alphabet[new_position]
    print(f'Here is your encoded text is :{cipher_text}')


while True:
    user_choice=input("Enter encode to encrypt and decode to decrypt \n")
    if user_choice=='encode':
        user_word_encode=input("Enter the word you want to encode?\n")
        shift_no=int(input("Enter the shift number?\n"))
        encrypt(user_word_encode,shift_no)

    elif user_choice=='decode':
        user_word_decode = input("Enter the word you want to decode?\n")
        shift_no = int(input("Enter the shift number?\n"))
        decrypt(user_word_decode,shift_no)

    else:
        print("Good bye")
        break
    user_play=input("Do you want to play again y/n ?\n")
    if user_play=="y":
        print('')
    else:
        break