# write a program that will print only alphabet from string without using any built in methods
string = input("Enter string").lower()
res = ""
for ch in string:
    if 'a'<= ch <= "z":
        res+=ch

print(res)

