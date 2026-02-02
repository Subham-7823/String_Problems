# Wtite a program that will print alphabet from string using while loop
#isalpha() is a method that is used to string is consist of alphabet or not
s = "engi_errin4"
res = ""
count = 0
while count < len(s):
    if s[count].isalpha():
        res += s[count]
    count += 1
print(res)