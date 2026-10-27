# conditional_tests.py
# Ten conditional tests using different operators.
#all predictions are written as comments before the print statements
user = "analyst"
role = "viewer"
failed = 3
port = 22


print("Is failed >= 3? ")# I predict True
print(failed >= 3)


print("\nIs user == 'analyst'? ")# I predict True
print(user == "analyst")


print("\nIs role == 'admin'? ")# I predict False
print(role == "admin")

print("\nIs port != 80? ")#I predict True
print(port != 80)


print("\nIs failed > 5? ")#I predict False 
print(failed > 5)


print("\nIs port < 1024? ")#I predict True
print(port < 1024)


print("\nIs role == 'viewer' and failed < 5?")#I predict True
print(role == "viewer" and failed < 5)

print("\nIs user == 'admin' or role == 'viewer'? ")#I predict True
print(user == "admin" or role == "viewer")


print("\nIs not (failed == 3)? ")#I predict False
print(not (failed == 3))


print("\nIs 0 <= port <= 65535?.")#I predict True
print(0 <= port <= 65535)