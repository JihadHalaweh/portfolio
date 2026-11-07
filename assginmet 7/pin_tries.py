# pin_tries.py
# Allow at most 3 tries to enter the correct PIN.

MAX_TRIES = 3
CORRECT_PIN = "2580"

tries = 0
while tries < MAX_TRIES:
    pin = input("PIN: ")
    tries += 1
    if pin == CORRECT_PIN:
        print("Access granted.")
        break
    else:
        print(f"Wrong PIN. Tries left: {MAX_TRIES - tries}")

if pin != CORRECT_PIN:
    print("Card blocked.")
