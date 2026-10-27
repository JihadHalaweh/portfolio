# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")
port = input("Port: ")

# Bug 1  (Runtime/Syntax): Changed assignment '=' to comparison '=='
is_admin = role == "admin"

# Bug 2  (Syntax): Corrected invalid operator '=<` to '<='
# Bug 3  (Semantic): Converted port to int() since input() returns a string
is_system_port = int(port) <= 1023

# Bug 4  (Semantic): Added full comparison on both sides of 'or'
is_web_port = int(port) == 80 or int(port) == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")