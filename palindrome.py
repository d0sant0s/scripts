str = input('Words please: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newstr = ''

str = str.lower()

for char in str:
  if char in alphabet:
    newstr += char

for letter in newstr:
  if len(newstr[:]) <= 1:
    print('Congrats! This is a palindrome')
    break
  elif newstr[0] == newstr[-1]:
    newstr = newstr[1:-1]
  else:
    print('This shit aint a palindrome ya dumb fuck!')
    break
