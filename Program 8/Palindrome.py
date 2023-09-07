class Palindrome:
    def is_palindrome(self, s):
        pass
class StringPalindrome(Palindrome):
    def is_palindrome(self, s):
        return s == s[::-1]
class NumberPalindrome(Palindrome):
    def is_palindrome(self, n):
        s = str(n)
        return s == s[::-1]
str_palindrome = StringPalindrome()
num_palindrome = NumberPalindrome()
print(str_palindrome.is_palindrome("madam"))
print(str_palindrome.is_palindrome("hello"))
print(num_palindrome.is_palindrome(12321))
print(num_palindrome.is_palindrome(56468))