Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # iterating by indexing
>>> list=["geeks","for","geeks"]
>>> for inex in list:
...       print(list[0:2])
... 
...       
['geeks', 'for']
['geeks', 'for']
['geeks', 'for']
>>> # continue statement
>>> for letter in 'geeks for geeks':
...     if letter=='e' or letter=='s':
...         continue
...     print("current letter"),letter
... 
...     
current letter
(None, 'g')
current letter
(None, 'k')
current letter
(None, ' ')
current letter
(None, 'f')
current letter
(None, 'o')
current letter
(None, 'r')
current letter
(None, ' ')
current letter
(None, 'g')
current letter
(None, 'k')
>>> 
>>> #break statement
>>> for letter in 'geeks for geeks':
...     if letter=='e' or letter=='s':
...         break
... 
>>> print("current letter"),letter
current letter
(None, 'e')
