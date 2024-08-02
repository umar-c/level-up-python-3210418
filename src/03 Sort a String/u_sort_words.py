def sort_string(string: str):
  strings = string.split()
  strings.sort(key=lambda strings: strings[0].lower())
  return ' '.join(strings)

if __name__ == '__main__':
  s = 'ORANGE banana Strawberry pineapple apple'
  print(sort_string(s))