import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to password generator!")
letter_in=int(input("How many letters would you like in your password?\n"))
numbers_in=int(input("How many letters would you like in your password?\n"))
symbols_in=int(input("How many letters would you like in your password?\n"))

letter_list=[]
number_list=[]
symbol_list=[]

for letter in range(letter_in):
    random_no=random.choice(letters)
    letter_list.append(random_no)
# print(letter_list)

for no in range(numbers_in):
    random_no=random.choice(numbers)
    number_list.append(random_no)
# print(number_list)

for special in range(symbols_in):
    random_no=random.choice(symbols)
    symbol_list.append(random_no)
# print(symbol_list)

combine_randomeness= letter_list+number_list+symbol_list
# print(combine_randomeness)
final_list=[]
for randomess in combine_randomeness:
    final_no=random.choice(combine_randomeness)
    final_list.append(final_no)
# print(final_list)

print("Your password is", end=' ')
# for i in range(len(final_list)):
#     print(f"Your password is {final_list[i]}",end=' ')
for password in final_list:
    print(f"{password}",end=' ')