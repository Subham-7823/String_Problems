#write a python program that will convert string lower to upper without using built in
#function
string="ahlfaFD"
res=""
for ch in string:
    if "a" <= ch <="z":
        res= res + chr(ord(ch)-32)
    else:
        res=res+ch
print(res)