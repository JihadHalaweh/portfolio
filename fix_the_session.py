# fix_the_session.py
# This program reports a user's session time.
    
username = input("Username: ")  #  there was a space at the start of the line
total_seconds = int(input("Session length in seconds: "))  # Wrapped input() in int() so math can be performed
    
minutes = total_seconds // 60  #  total_seconds is now an int (used // for clean integer division)
seconds = total_seconds % 60
    
print("=" * 30)
print(f"User: {username}")  #  Added 'f' prefix to evaluate the variable inside curly braces
print(f"Session: {minutes} min {seconds} s") # Used an f-string to prevent TypeErrors 
print("=" * 30)