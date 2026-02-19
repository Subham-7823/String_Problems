#Write a python program that print the index of substring
string = input()
sub_String = input()
if sub_String in string:
    print(string.find(sub_String)+1)#find method is used to find index
else:
    print("-1")
    