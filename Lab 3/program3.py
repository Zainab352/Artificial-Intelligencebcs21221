Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def main():
...      number = random.randint(1, 9)
...      guess = None
...      while guess != number:
...          guess = int(input('Guess a number between 1 and 9: '))
...          if guess == number:
...              print('Well guessed!')
... 
>>> 
>>> main()
Guess a number between 1 and 9: 10
Guess a number between 1 and 9: 5
Guess a number between 1 and 9: 6
Guess a number between 1 and 9: 7
Guess a number between 1 and 9: 9
Guess a number between 1 and 9: 4
Guess a number between 1 and 9: 3
Guess a number between 1 and 9: 2
Guess a number between 1 and 9: 5
Guess a number between 1 and 9: 5
Guess a number between 1 and 9: 4
Guess a number between 1 and 9: 3
Guess a number between 1 and 9: 8
Well guessed!
