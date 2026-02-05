#write a program that will print special charecters from string
string = "sadjflh$763!@"
res=""
for ch in string:
    if not("a"<=ch<="z"or"A"<=ch<="Z"or"0"<=ch<="9"):
        res+=ch
print(res)