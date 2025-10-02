"""
File: caesar.py
Name: Annie Huang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program deciphers the string.
    """
    number = int(input('Secret number: '))
    old = input("What's the cipher string? ")
    new = decipher(old, number)
    print(input('The deciphered string is: ' + new))


def decipher(old, number):
    """
    :return: str, the deciphered string.
    """
    new_alphabet = ''
    upper = ''
    ans = ''
    for i in range(len(ALPHABET)):  # find the new order of alphabet
        if i < number:
            ch = ALPHABET[len(ALPHABET) - number + i]
        else:
            ch = ALPHABET[i - number]
        new_alphabet += ch

    for i in range(len(old)):  # change lowercase to uppercase
        ch = old[i]
        if ch.islower():
            upper += ch.upper()
        else:
            upper += ch

    for i in range(len(upper)):  # decipher the string
        ch = upper[i]
        if ch not in new_alphabet:
            ans += ch
        else:
            position = new_alphabet.find(ch)
            ans += ALPHABET[position]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
