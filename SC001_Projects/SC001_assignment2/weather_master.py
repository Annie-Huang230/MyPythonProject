"""
File: weather_master.py
Name: Annie Huang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -1


def main():
	"""
	This program computes the highest/lowest/average temperatures.
	"""
	print("stanCode \"Weather Master 4.0\"!")
	temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	count = 0
	total = 0
	cold = 0
	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		total = total + temperature
		highest = temperature
		lowest = temperature
		if temperature < 16:
			cold += 1
		while True:
			count += 1
			temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if temperature == EXIT:
				break
			else:
				total = total + temperature
				if temperature < 16:
					cold += 1
				if temperature > highest:
					highest = temperature
				if temperature < lowest:
					lowest = temperature
		avg = float(total / count)
		print('Highest Temperature = ' + str(highest))
		print('Lowest Temperature = ' + str(lowest))
		print('Average: ' + str(avg))
		print(str(cold) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
