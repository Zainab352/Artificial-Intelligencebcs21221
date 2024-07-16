Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = input("Enter a word: ")
Enter a word: zarish
>>> reverse = ''
>>> for i in range(len(word) - 1, -1, -1):
...     reverse += word[i]
... 
>>> print("Reverse of the word is: "),reverse
Reverse of the word is: 
(None, 'hsiraz')
