import random
ANSWERS = [
  'yes - definitely',
  'It is decidedly so.',
  'Without a doubt.',
  'Reply hazy, try again.',
  'Ask again later.',
  'Better not tell you now.',
  'My sources say no.',
  'Outlook not so good.',
  'Very doubtful.'
]
answer = random.choice(ANSWERS)

print('Please give your name, and question')

name = input('Name: ')
question = input('Question: ')

if name != "":
  print(f"{name} asks '{question}'")
if question == '':
  print('Please. Ask a question')
else:
  print(f'Magic 8-Ball says: {answer}')
