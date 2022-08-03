import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','#','$','&','*']
numbers = ['1','2','3','4','5','6','7','8','9','0']

letter_size = int(input("Enter how many letters do you want: "))
number_size = int(input("Enter how many numbers do you want: "))
symbol_size = int(input("Enter how many symbols do you want: "))

password_list = []
password = "" 

for letter in range (1 ,letter_size+1):
    val = random.choice(letters)
    password_list += val
for number in range (1 ,number_size+1):
    val = random.choice(numbers)
    password_list += val
for symbol in range (1 ,symbol_size+1):
    val = random.choice(symbols)
    password_list += val
    
random.shuffle(password_list)

for i in password_list:
    password += i
print(f"Your new password is: {password}")