alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(direction: str, start_text: str, cipher_key: int):
    end_text = ""
    if direction == 'decrypt':
        cipher_key *= -1
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = (position + cipher_key) % 26
            end_text += alphabet[new_position]
    print(end_text)

should_continue = True
while should_continue:
    print("Welcome to Ceaser Cipher! \n")
    option = input("Enter 'encrypt' for encryption and 'decrypt' for decryption!\n")
    text = input(f"Please input the text to be {option}ed: \n")
    key = int(input("Please input the key: \n")).__abs__()
    ceaser(option, text, key)
    print("\n")
    ask = input("Do you want to continue? Type 'Y' for yes or 'N' for no:\n")
    if ask.lower() == 'n':
        should_continue = False
        print("Goodbye!")
    print("\n")
