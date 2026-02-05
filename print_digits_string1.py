#write a program that will only print numbers from string without using builtin methods
string = "swdflfu235kjjkSARG34*7a36"
numbers = ""
for ch in string:
    if "0" <= ch <= "9":
        numbers+=ch
print(numbers)