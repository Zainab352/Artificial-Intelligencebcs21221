Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(7):
...     if i == 3 or i == 6:
...         continue
...     print(i, end=' ')
... 
...     
0 1 2 4 5 
