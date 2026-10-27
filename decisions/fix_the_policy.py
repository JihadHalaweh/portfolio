# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Bug 1  (Syntax): Added missing colon ':'
# Bug 2 (Semantic): Changed 'elif' to separate 'if' so all rules are reported
if len(password) < MIN_LENGTH:
    print("- Too short.")
if password == username:
    print("- Same as the username.")

# Bug 3  (Semantic): Ordered tests from strictest/narrowest (>= 16) first
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

# Bug 4  (Semantic/Syntax): Unindented print statement to run for all classifications
print(f"Length: {len(password)} ({strength})")