#write a function called isphonenumber to recognise a pattern 
# 415-555-4242 without using regular expression 
def isphonenumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isnumeric():
            return False
        if text[3]!='-':
            return False
        for i in range (8,12):
            if not text[i].isnumeric():
                return False
            return True
#test the isphnenumber function
phone_number='415-555-4242'
if isphonenumber(phone_number):
    print('The phone number {} is valid'.format(phone_number))
else:
    print('The phone number {} is not valid '.format(phone_number))
