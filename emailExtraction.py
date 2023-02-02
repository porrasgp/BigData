import re

emails = []
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line)
        if match:
            emails.append(match.group())

print(emails)
