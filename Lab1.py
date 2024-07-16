Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hellow,Word")
Hellow,Word
>>> x=1
>>> # the initial value of x is 1.
>>> if x>0:
...     print("these are two comments")#print a string
... 
...     
these are two comments
>>> # Multiple statements in a single line
>>> print("statements1")
statements1
>>> print("statement2")
statement2
>>> # we can write these statements on a single line as .
>>> print("statement1");print("statement2")
statement1
statement2
>>> #identation
>>> y=1
>>> if y>0:
... print("The statement with no identation")
SyntaxError: expected an indented block after 'if' statement on line 1
>>> if y>0
SyntaxError: expected ':'
>>> if y>0:
...  print("The statement with a single space identation")
...  print("The statement with single space identation")
... 
...  
The statement with a single space identation
The statement with single space identation
>>> if y>0:
...     print("The statement with single tsb identation")
... 
...     
The statement with single tsb identation
>>> if y>0:
...      print("The statement with single space+identation")
...      print("The statement with single space+tab identation")
... 
...      
The statement with single space+identation
The statement with single space+tab identation
>>> a=1234
>>> type(a)
<class 'int'>
b=-1234
type(b)
<class 'int'>
c=1.23
type(c)
<class 'float'>
k=12.2e-10
type(k)
<class 'float'>
s=25E23
type(s)
<class 'float'>
x = complex(1,2)
print(x)
(1+2j)
z=1+2j
type(z)
<class 'complex'>
z=1+2J
type(z)
<class 'complex'>
x=True
type(True)
<class 'bool'>
y=False
type(y)
<class 'bool'>
str1="string" #string start and end with double coutes.
print(str1)
string
str2='string2'#string start and end eith singl and single coutes
print(str2)
string2
str3='day"' #string within a double qoutes
print(str3)
day"
str4="day's" # string single qoutes  within a double qoute
print(str4)
day's
print("This ia a backslash (\\) mark")
This ia a backslash (\) mark
print("This is a tab \t key")
This is a tab 	 key
print("This ia a new line \n new line")
This ia a new line 
 new line
print("this is a \'single\' qoutes")
this is a 'single' qoutes
print("this is a \"doble\" qoutes")
this is a "doble" qoutes







#string arrayindices and accessing string  elements
str1="python Tutorial"
print(str[0]) #print first character.
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(str[0]) #print first character.
TypeError: type 'str' is not subscriptable
print(str1[0])# print first character.
p
print(str1[-15])# print first character.
p
print(str1[6])# print sixth character.
 


print(str1[6])# print sixth character.
 
print(str1[2])# print second character.
t
print(str1[7])# print seventh character.
T
print(str1[-8])# print seventh character.
T
# slicing a string
print(str1[4:8])
on T
# creating a list
my_list = [1,2,3,4,5]
print(my_list)
[1, 2, 3, 4, 5]
my_list1 = ['red','blu','black',]
print(my_list1)
['red', 'blu', 'black']
my_list2 = ['red','blue',2,3,4,]
print(my_list2)
['red', 'blue', 2, 3, 4]
my_list3 = []
print(my_list3)
[]
# list indices
print(my_list1[2])
black
print(my_list2[1])
blue
# list slicing
print(my_list2[1:3])
['blue', 2]
print(my_list1[1:2])
['blu']
