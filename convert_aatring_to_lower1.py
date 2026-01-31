#write a python code that wll convert upper to lower without using built in function
#ascii of a = 97 and A = 65 
string = "sdhkvAREA23"
res=""
for ch in string:
    if "A" <= ch <= "Z":
        res = res + chr(ord(ch)+32)
    else:
        res=res+ch
print(res)