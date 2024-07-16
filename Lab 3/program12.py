Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     lines = []
...     while True:
...         line = input("Enter a line: ")
...         if line == "":
...             break
...         lines.append(line)
...     for line in lines:
...          print(line.lower())
... 
>>> main()
Enter a line:  my name zanairish
Enter a line: my name esha
Enter a line: 010000111010100111001001
Enter a line: 1010
Enter a line: 0100,0011,1010,1001,1100,1001
Enter a line: 0100,0011,1010,1001,1100,1001,
