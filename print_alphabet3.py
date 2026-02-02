#write a program to print alphabets from string using for loop
string = input("Enter your string")
res= ""
for ch in string:
    if "a" <= ch <= "z"  or "A" <=ch <= "Z":
        res+=ch
print(res)