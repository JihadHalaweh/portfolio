"""
int(" 22 ") will WORK.
Reason: Leading and trailing whitespace characters in the string are allowed 
and will be stripped before conversion.
"""
"""
int("+22") will WORK.
Reason: The string can be preceded by an optional '+' or '-' sign to 
indicate whether the number is positive or negative.
"""
"""
int("0022") will WORK.
Reason: Leading zeros are permitted for base-10 strings and will simply be 
evaluated as a standard integer (22).
"""
"""
int("2_2") will FAIL.
Reason: While underscores are allowed in numeric literals in Python code (like 1_000), 
they are not permitted inside strings passed to int() and will raise a ValueError.
"""

# Testing each string

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
# print(int("2_2"))  Uncommenting this line will lead to  a ValueError


# Documentation: https://docs.python.org/3/library/functions.html#int
