# risk_score.py
# Calculate a login risk score based on multiple security factors.

score = 0

failed_hour = int(input("Failed attempts in the last hour: "))
login_hour = int(input("Login hour (0-23): "))
new_device = input("New device (yes/no): ")

# Separate if statements because multiple risk factors can apply at once
if failed_hour >= 3:
    score += 40

if login_hour < 6:
    score += 30

if new_device == "yes":
    score += 30

# Chain to classify the final score
if score >= 70:
    level = "HIGH"
elif score >= 30:
    level = "MEDIUM"
else:
    level = "LOW"

print(f"Risk score: {score} ({level})")