# fix_the_stats.py
# Count failed logins and the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1  Initialize failed before the loop so it accumulates properly instead of resetting to 0 each iteration.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2 : Use float division / instead of integer division // to produce 30.0.
# Bug 3 : Move the print statement outside the loop so it prints the average once after all values are processed.
print(f"Average session: {total / count} minutes")

# Bug 4 : Change range(1, 4) to range(1, 5) so that Level 4 is included in the output.
for level in range(1, 5):
    print(f"Level {level}")
