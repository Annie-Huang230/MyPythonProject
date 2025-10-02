"""
File: string_score.py
Name: Annie Huang
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    This program counts the total score of the string.
    """
    score('1aB4rC')  # digit->1 ; upper->2; lower->3
    # 12
    print(score('1aB4rC'))
    score('aaaaA3')
    # 15
    print(score('aaaaA3'))


def score(string):
    """
    :return: int, the total score
    """
    count = 0
    for i in range(len(string)):
        ch = string[i]
        if ch.isdigit():
            count = count + 1
        if ch.isupper():
            count += 2
        if ch.islower():
            count += 3
    return count


if __name__ == '__main__':
    main()
