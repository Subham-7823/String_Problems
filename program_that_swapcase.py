#write a program that will swap the case
string = "arfhbq245,akAREGTQgnqoiu3"
res=""
for ch in string:
    if "a" <= ch <="z":
        ch = chr(ord(ch)-32)
        res = res+ch
    elif "A" <= ch <= "Z":
        ch=chr(ord(ch)+32)
        res = res+ch
    else:
        res=res+ch
print(res)
