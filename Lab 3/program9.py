Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a, b = 0, 1
>>> while b < 50:
...      print(b, end=' ')
...      a, b = b, a + b
... 
...      
1 1 2 3 5 8 13 21 34 
