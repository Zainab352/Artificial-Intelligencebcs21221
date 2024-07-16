Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def my_function():
    print("Hello from a function")

my_function()
Hello from a function

# Parameters
def my_function(fname):
    print(fname + " Refsnes")
... 
>>> my_function("Emil");my_function("Tobais");my_function("Linus")
Emil Refsnes
Tobais Refsnes
Linus Refsnes
>>> 
>>> 
>>> # Default parameter values
>>> 
>>> def my_function(country="norway"):
...     print("i am from" + country)
... 
>>> my_function("sweeden");my_function("india");my_function();my_function("Barazeel")
i am fromsweeden
i am fromindia
i am fromnorway
i am fromBarazeel
>>> 
>>> 
>>> #Passing a List as a Parameter
>>> def my_function(food):
...     for x in food:
...         print(x)
... 
>>> 
>>> fruits = ["apple", "banana", "cherry"] ;my_function(fruits)
apple
banana
cherry
>>> 
>>> #Return Values
>>> def my_function(x):
...     return 5 * x
... 
>>> print(my_function(3));print(my_function(5));print(my_function(9))
15
25
45
>>> 
>>> 
>>> #Keyword Arguments
>>> 
>>> def my_function(child3, child2, child1):
...     print("The youngest child is " + child3)
... 
>>> my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
The youngest child is Linus
