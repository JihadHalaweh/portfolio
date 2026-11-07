# port_report.py
# Report IANA port ranges for a specified port interval.

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

count = 0
for port in range(start_port, end_port + 1):
    count += 1
    if port <= 1023:
        category = "system"
    elif port <= 49151:
        category = "user"
    else:
        category = "dynamic"
    print(f"{port}: {category}")

print(f"Ports checked: {count}")
