from cs50 import get_int
from cs50 import get_string

# Prompt user for credit card number
credit_num = get_int("Number: ")

# Check if length of credit card number is valid

# Set variables needed for check
i = credit_num
length = 0

# Determine length of credit card number
while i >= 1:
    i = i / 10
    length += 1

# Check if length is valid
if length != 13 and length != 15 and length != 16:
    print("INVALID")

# Check Sum Calculation

# Set variables needed for check
j = credit_num
sum1 = 0
sum2 = 0

t = credit_num % 10
s = int(credit_num / 10)
print(s)

# Check Sum
while j >= 1:

    # Calculate Sum1
    rem1 = j % 10
    j = int(j / 10)
    sum1 = sum1 + rem1

    # Calculate Sum2
    rem2 = j % 10
    j = int(j / 10)

    rem2 = rem2 * 2
    x1 = int(rem2 % 10)
    x2 = int(rem2 / 10)
    sum2 = sum2 + x1 + x2

check_sum = sum1 + sum2
print(check_sum)

# Check that check sum value is valid
r = check_sum % 10

if r != 0:
    print("INVALID")

# Check if VISA, AMEX, or MASTERCARD
start = credit_num

while (start > 100):
    start = int(start / 10)

if ((int(start / 10) == 3) and ((start % 10 == 4) or (start % 10 == 7))):
    print("AMEX")
elif ((int(start / 10) == 5) and ((0 < start % 10) and (start % 10 < 6))):
    print("MASTERCARD")
elif (int(start / 10) == 4):
    print("VISA")
else:
    print("INVALID")
