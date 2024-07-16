Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = 5
>>> for i in range(1, n + 1):
...     for j in range(1, i + 1):
...         print('*', end='')
...     print()
...     for i in range(n - 1, 0, -1):
...         for j in range(1, i + 1):
...             print('*', end='')
...         print()
... 
...         
*
****
***
**
*
**
****
***
**
*
***
****
***
**
*
****
****
***
**
*
*****
****
***
**
*
