# truth_research.py
# Researching truth values in Python.
# Reference: Python Documentation - Built-in Types (Truth Value Testing)
# https://docs.python.org/3/library/stdtypes.html

# Predictions (in comments):
# bool("") -> False (empty sequence)
# bool("0") -> True (non-empty string)
# bool(0) -> False (zero numeric value)
# bool(0.0) -> False (zero float value)
# bool("False") -> True (non-empty string, even if text says "False")

print(bool(""))
print(bool("0"))
print(bool(0))
print(bool(0.0))
print(bool("False"))