#generate the same code but dont use any methods
string = input("Enter a string")
res = ""
for i in string:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        res+=i
print(res)