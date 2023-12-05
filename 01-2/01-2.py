# https://adventofcode.com/2023/day/1#part2

def readLinesFromFile(fileName):
	with open(fileName, 'r') as file:
		lines = file.readlines()
	# clean line ends from lines
	return [line.strip() for line in lines]

def convert_to_numeric(numberAsString: str):
    # Dictionary mapping spelled-out digits to their numerical values
    digit_mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                     'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Return the corresponding numerical value or the original character if not a spelled-out digit
    return digit_mapping.get(numberAsString)

def calcCalibrationValue(fileName):
	lines = readLinesFromFile(fileName)
	calibrationSum = 0

	for line in lines:
        # Extract the first and last characters from each word in the line
		firstChar = next(char for char in line if char.isalpha() or char.isdigit())
		lastChar = next(char for char in reversed(line) if char.isalpha() or char.isdigit())

        # Convert the characters to their numerical equivalents
		firstDigit = convert_to_numeric(firstChar)
		lastDigit = convert_to_numeric(lastChar)

        # Form a two-digit number and add it to the sum
		calibrationValue = int(str(firstDigit) + str(lastDigit))		
		calibrationSum += calibrationValue;
		print('line: {0}, firstDigit: {1}, lastDigit: {2}, calibrationValue: {3}'.format(line, firstDigit, lastDigit, calibrationValue))

	return calibrationSum

calibrationSum = calcCalibrationValue("01-2\input.txt")
print("Calibration sum: ", calibrationSum)
