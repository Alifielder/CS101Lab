import string
def encrypt(string_text, int_key):
    newString=''
    for i in string_text:
        newString+=chr(ord(i)+int_key)
    print(newString)
def decrypt(string_text, int_key):
    newDecrypt=''
    for i in string_text:
        newDecrypt=chr(ord(i)+int_key)
    print(newDecrypt)
def get_input():
    choice=input('How would you like to proceed?: ')
    main()
def print_Menu():
    print(' 1)Encode a string \n 2)Decode a string\n Q)Quit')
print_Menu()
def main():
    Again= True
    while Again:
        choice=get_input()
        if choice=='1':
            string_text= input("Enter a (brief) text to encrypt: ").upper()
            key=int(input('Enter the number to shift letters by: '))
            cipherText=encrypt(string_text,key)
            print("Encrypted: ", cipherText)
        elif choice=='2':            
            string_text= input("Enter a (brief) text to decrypt: ").upper()
            key=int(input('Enter the number to shift letters by: '))
            cipherText=decrypt(string_text,key)
            print("Decrypted: ", cipherText)
        elif choice=='Q' or choice=='q': 
            print("Have a good day!")
            Again=False
main()
