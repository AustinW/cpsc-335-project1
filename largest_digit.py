
def largest_digit(s):
     max_digit = -1
     for digit in s:
          if digit.isdigit() and int(digit) > max_digit:
               max_digit = int(digit)
     if max_digit >= 0:
          return max_digit
     else:
          return None

print(largest_digit("sdk2skl"))