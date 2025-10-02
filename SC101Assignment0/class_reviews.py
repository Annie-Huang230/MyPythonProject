"""
File: class_reviews.py
Name: Annie Huang
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1  # Constant value to indicate the exit signal when the user enters "-1"


def main():
    """
    This program calculates the scores for two classes: SC001 and SC101.
    The program will prompt the user to input a class name and score,
    then compute the maximum, minimum, and average scores for each class.
    The program will continue to accept input until the user enters "-1".
    """
    name1 = input('Which class? ')
    name1 = name1.lower()  # convert the input string into lowercase
    count = 0
    total = 0
    count_1 = 0
    total_1 = 0
    minimum = float('inf')  # 無窮大
    maximum = -float('inf')  # 無窮小 = 負的無窮大
    minimum_1 = float('inf')
    maximum_1 = -float('inf')

    # If the user enters "-1" immediately, terminate the program with a message
    if name1 == str(EXIT):
        print('No class scores were entered')  # if the first entered name is EXIT
    else:
        # If a valid class is entered, prompt for the score
        score = int(input('Score: '))

        # Process the first class name (either SC001 or SC101)
        if name1 == 'sc001':
            count += 1
            total = total + score
            maximum = score  # Set the first score as both the maximum and minimum for SC001
            minimum = score
        else:
            count_1 += 1
            total_1 = total_1 + score
            maximum_1 = score  # Set the first score as both the maximum and minimum for SC101
            minimum_1 = score

        # Start the loop where the program asks for further class names and scores
        while True:
            name = input('Which class? ')
            name = name.lower()  # convert the input string into lowercase

            # If the user enters "-1", exit the loop and display the results
            if name == str(EXIT):
                break
            else:
                score2 = int(input('Score: '))
                # if the first entered class name is not sc001, set score2 as the initial maximum/minimum for SC001
                if count == 0:
                    maximum = score2
                    minimum = score2
                # if the first entered class name is not sc101, set score2 as the initial maximum/minimum for SC101
                if count_1 == 0:
                    maximum_1 = score2
                    minimum_1 = score2

                if name == 'sc001':
                    if score2 > maximum:
                        maximum = score2  # Update the maximum if the new score is higher
                    if score2 < minimum:
                        minimum = score2
                    count += 1
                    total = total + score2  # Update the minimum if the new score is lower
                if name == 'sc101':
                    if score2 > maximum_1:
                        maximum_1 = score2
                    if score2 < minimum_1:
                        minimum_1 = score2
                    count_1 += 1
                    total_1 = total_1 + score2

        # After the loop ends, print the statistics for SC001/SC101
        if count == 0:
            print('=============SC001=============')
            print('No score for SC001')
        else:
            avg = float(total / count)
            print('=============SC001=============')
            print('Max (001): ' + str(maximum))
            print('Min (001): ' + str(minimum))
            print('Avg (001): ' + str(avg))

        if count_1 == 0:
            print('=============SC101=============')
            print('No score for SC101')
        else:
            avg_1 = float(total_1 / count_1)
            print('=============SC101=============')
            print('Max (101): ' + str(maximum_1))
            print('Min (101): ' + str(minimum_1))
            print('Avg (101): ' + str(avg_1))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
