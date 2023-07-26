from difflib import SequenceMatcher
str1=input("Enter string 1:")
str2=input("Enter string 2:")
similarity=SequenceMatcher(None,str1,str2).ratio()
print("original string:")
print(str1)
print(str2)
print("similarity between two Strings:")
print(similarity)