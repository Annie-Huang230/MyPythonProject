"""
File: prime_checker.py
Name: Annie Huang
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -10


def main():
    """
    This program finds the prime numbers.
    """
    print('Welcome to the prime checker!')

    while True:
        n = int(input('n: '))
        if n == EXIT:
            break
        else:
            n1 = 2
            while n1 != n:
                if n % n1 == 0:
                    break
                else:
                    n1 = n1 + 1
            if n1 == n:
                print(str(n) + ' is a prime number.')
            else:
                print(str(n) + ' is not a prime number.')
    print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
