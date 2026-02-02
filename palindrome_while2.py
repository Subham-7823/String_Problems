#write a program to check string is palindrome or not using while loop
string = "subham"
count = len(string)-1
res=""
while count >= 0:
    res = res + string[count]
    count=count-1
if res == string :
    print("String is palindrome")
else:
    print("string is not palindrome")