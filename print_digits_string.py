#write a program to print digits of a string using builtin methods
string = input("Enter a string")
res=""
for ch in string:
    if ch.isdigit():
        res+=ch
print("Your entered string is ",string)
print()
print("Numbers in string are ",res)
