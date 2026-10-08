import re

text = "My emails are diya123@gmail.com and student123@yahoo.com"

pattern = r'[\w.-]+@[\w.-]+\.\w+'

emails = re.findall(pattern, text)

print("Email addresses found:")
print(emails)