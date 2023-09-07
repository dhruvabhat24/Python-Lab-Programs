#Develop a python program that colud search the text us a file for email addresses and phone numbers.
import re
phone_number = re.compile(r'\+\d{10,12}')
email_pattern = re.compile(r'\b[w.-]+@[\w.-]+\.\w{2,6}\b')
filename='s.txt'
with open (filename,'r') as file:
    text = file.read()

phone_numbers = phone_number.findall(text)
if phone_numbers:
    print("phone numbers found: ")
    for number in phone_numbers:
        print(phone_number)
email__addresses=email_pattern.findall(text)
if email__addresses:
    print("email addresses found: ")
    for address in email__addresses:
        print(email__addresses)
