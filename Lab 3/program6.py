Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> count_even = 0
>>> count_odd = 0
>>> 
>>> for i in numbers:
...      if i % 2 == 0:
...             count_even += 1
...      else:
...          count_odd += 1
... 
>>> print("Number of even numbers:"),count_even;print("Number of odd numbers:"),count_odd
Number of even numbers:
(None, 4)
Number of odd numbers:
(None, 5)
