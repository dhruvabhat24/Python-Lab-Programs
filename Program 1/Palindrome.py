num=int(input("Enter the number :"))
num_str=str(num)
if num_str==num_str[::-1]:
 print("num is a palindrome ")
else:
 print("num is not a palindrome")
digit_count={  }
for digit in  num_str:
 if digit in digit_count:
  digit_count[digit]+=1
else:
 digit_count[digit]=1
 print("Digit Count")
 for digit,count in digit_count.items():
  print(digit,":",count)