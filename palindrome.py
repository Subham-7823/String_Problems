# write a program to check string is palindrome or not

test = "madam"
res=""
for ch in test:
    res=ch+res
if test == res:
    print("String is palindrome")
else:
    print("String is not palindrome")
