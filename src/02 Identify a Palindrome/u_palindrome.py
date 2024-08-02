import re

def is_palindrome(string: str):
  string = string.replace(' ', '').replace('.', '').replace('!', '').replace(',', '').replace('\'', '').lower()
  return string == string[::-1]

def is_palindromeV2(string: str):
  string = ''.join(re.findall(r'[a-z]+', string.lower()))
  return string == string[::-1]

if __name__ == '__main__':
    strings = ['level', 'Level', 'hello world', "Go hang a salami, I'm a lasagna hog!"]
    for s in strings:
      print(f"{s} is a palindrome (v1) = {is_palindrome(s)}")
      print(f"{s} is a palindrome (v2) = {is_palindromeV2(s)}")