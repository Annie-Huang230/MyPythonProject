"""
File: complement.py
Name: Annie Huang
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program finds the the complement strand of a DNA sequence.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :return: str, the complement strand of a DNA sequence
    """
    if len(dna) == 0:
        ans = 'DNA strand is missing.'
    else:
        ans = ''
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                ans += 'T'
            elif ch == 'T':
                ans += 'A'
            elif ch == 'G':
                ans += 'C'
            else:
                ans += 'G'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
