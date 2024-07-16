Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dataList = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {11:'V', 12:'A'}]
... 
>>> for i in dataList:
...      print(i, type(i))
... 
...      
1452 <class 'int'>
11.23 <class 'float'>
(1+2j) <class 'complex'>
True <class 'bool'>
w3resource <class 'str'>
(0, -1) <class 'tuple'>
[5, 12] <class 'list'>
{11: 'V', 12: 'A'} <class 'dict'>
