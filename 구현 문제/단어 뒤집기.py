s = list(input())
tag = False
word = ''
result = ''
for i in s:
  if not tag:
    if i == '<':
      tag = True
      word = word + i
    elif i == ' ':
      word = word + i
      result = result + word
      word = ''
    else:
      word = i + word
  elif tag:
    word = word + i
    if i == '>':
      tag = False
      result = result + word
      word = ''

print(result+word)