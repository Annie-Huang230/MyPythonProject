"""
File: webcrawler.py
Name: Annie Huang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('tr')
        male_total = 0
        female_total = 0
        for tag in tags[2:]:  # Skip the first 2 rows
            tokens = tag.text.split()  # Extract the text and split into tokens
            if len(tokens) == 5:
                # Remove comma and join back into a single string
                male_num = tokens[2].split(',')
                female_num = tokens[4].split(',')
                male_total += int(''.join(male_num))
                female_total += int(''.join(female_num))

        print('Male Number:', male_total)
        print('Female Number:', female_total)


if __name__ == '__main__':
    main()
