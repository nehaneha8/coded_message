alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(text, shifty, direction):
    mpty = ""
    for i in text:
        if i in alphabet:
            x = alphabet.index(i)
            if direction == "decrypt":
                if shifty < 0:
                    shifty *= 1
                elif shifty > 0:
                    shifty *= -1
            if i in alphabet:
                new_pos = x + shifty
                mpty += alphabet[new_pos]
        else:
            mpty += i
    print(f"The {direction}ed text is {mpty}")

end = False
while not end:
    e_or_d = input("Would you like to encrypt or decrypt a message?").lower()
    message = input("What is the message? ").lower().strip()
    shift = int(input("What is the letter shift? "))
    shift = shift % 26

    caesar(text=message, shifty=shift, direction=e_or_d)

    restart = input("Would you like to restart? Yes or no. ").lower()
    if restart == "no":
        end = True
        print("Goodbye")