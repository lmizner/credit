# credit

CS50 Problem Set: https://cs50.harvard.edu/x/2021/psets/1/credit/

This program prompts the user for a credit card number and then reports whether it is a valid American Express, MasterCard, or Visa card number based on the definitions of each's format and structure. 

All American Express numbers start with 34 or 37, most MasterCard numbers start with 51, 52, 53, 54, or 55, and all Visa 
numbers start with 4. Credit card numbers also have a checksum value built into them. A checksum is a mathematical 
relationship between at least one number and the others. By checking the starting value and the checksum value we can 
validate which type of credit card the number belongs to or if the number is invalid. 

The checksum is calculated using the Luhn's algorithm to determine if the credit card number is valid. The steps for 
calculation in the program are as follows:
  1. Mutliply every other digit by 2, starting with the number's second-to-last digit, and then add those products' 
     digits together.
  2. Add the sume to the sum of the digits that weren't multiplied by 2. 
  3. If the total's last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the 
     number is valid.







