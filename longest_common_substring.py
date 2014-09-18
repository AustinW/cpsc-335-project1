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

print(longest_repeated_substring("banana"))