# https://adventofcode.com/2023/day/1

def readLinesFromFile(fileName):
	with open(fileName, 'r') as file:
		lines = file.readlines()
	# clean line ends from lines
	return [line.strip() for line in lines]


def calcCalibrationValue():
	lines = readLinesFromFile("input.txt")
	calibrationSum = 0

	for line in lines:
		firstDigit = next(char for char in line if char.isdigit())
		lastDigit = next(char for char in reversed(line) if char.isdigit())
		calibrationValue = int(firstDigit + lastDigit);
		calibrationSum += calibrationValue;
		print('line: {0}, firstDigit: {1}, lastDigit: {2}, calibrationValue: {3}'.format(line, firstDigit, lastDigit, calibrationValue))

	return calibrationSum

calibrationSum = calcCalibrationValue()
print("Calibration sum: ", calibrationSum)
