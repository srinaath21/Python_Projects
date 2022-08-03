print('''

 dP""b8    db    888888 .dP"Y8 888888 88""Yb      dP""b8 88 88""Yb 88  88 888888 88""Yb 
dP   `"   dPYb   88__   `Ybo." 88__   88__dP     dP   `" 88 88__dP 88  88 88__   88__dP 
Yb       dP__Yb  88""   o.`Y8b 88""   88"Yb      Yb      88 88"""  888888 88""   88"Yb  
 YboodP dP""""Yb 888888 8bodP' 888888 88  Yb      YboodP 88 88     88  88 888888 88  Yb 

''')


def encode(word):
    encoded = ""
    for i in word:
        val = ord(i)
        val += shift_number
        encoded += chr(val)
    print(f"The result of your encoded message is {encoded}")

def decode(word):
    decoded = ""
    for i in word:
        val = ord(i)
        val -= shift_number
        decoded += chr(abs(val))
    print(f"The result of your decoded message is {decoded}")

word = input("Enter a word: ")
shift_number = int(input("enter a shift number: "))
if shift_number > 25:
            shift_number %= 25  
choice = input("type 1 to encode and type 2 to decode: ")

if choice == '1':
    encode(word)
if choice == '2':
    decode(word)
if choice != '2' and choice != '1':
    print("wrong choice")
