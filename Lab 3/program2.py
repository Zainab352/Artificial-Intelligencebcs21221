Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def celsius_to_fahrenheit(C):
...      return (C * 9/5) + 32
... 
>>> def fahrenheit_to_celsius(F):
...      return (F - 32) * 5/9
... 
>>> def main():
...     celsius = 60
...     fahrenheit = 45
...     print(f'{celsius}°C is {celsius_to_fahrenheit(celsius)} in Fahrenheit')
...     print(f'{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)} in Celsius')
... 
>>> main()
60°C is 140.0 in Fahrenheit
45°F is 7.222222222222222 in Celsius
