
import sys
import time

def largest_digit(subject):
	max_digit = -1
	for digit in subject:
		if digit.isdigit() and int(digit) > max_digit:
			max_digit = int(digit)
	if max_digit >= 0:
		return max_digit
	else:
		return None

def longest_repeated_substring(subject):
	length = len(subject)
	substrList = []

	longestSubstring = ""

	for i in range(length):
		for j in range(i,length):
			substrList.append(subject[i:j])

	for i in range(len(substrList)):
		for j in range(i + 1, len(substrList)):

			if substrList[i] == substrList[j] and len(substrList[i]) > len(longestSubstring):
				longestSubstring = substrList[i]

	return longestSubstring

def main():
	if len(sys.argv) != 3:
		print('error: you must supply exactly two arguments\n\n' +
			  'usage: python3 <Python source code file> <text file> <n>')
		sys.exit(1)

	filename = sys.argv[1]
	n = int(sys.argv[2])

	entire_file = open(filename).read()
	print('Loaded "' + filename + '" of length ' + str(len(entire_file)))

	# take only the first n characters of entire_file
	s = entire_file[:n]
	assert(len(s) == n)

	# Algorithm 1
	start = time.perf_counter()
	x = largest_digit(s)
	end = time.perf_counter()
	print('largest digit = ' + str(x))
	print('elapsed time = ' + str(end - start))

	# Algorithm 2
	start = time.perf_counter()
	x = longest_repeated_substring(s)
	end = time.perf_counter()
	print('longest repeated substring = "' + str(x) + '"')
	print('elapsed time = ' + str(end - start))

if __name__ == '__main__':
	main()
