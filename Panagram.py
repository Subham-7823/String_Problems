# Write a program to check number is panagram or not
#LOGIC
#if in a sentence all charecters from a -  z , present atlest once then it is called panagram

# Step 1: Convert the sentence to lowercase
# Step 2: Ignore spaces and special characters
# Step 3: Check if every letter from a to z is present
string="a quick br54own fox jumps over the lazy dog "
for ch in range(ord('a'),ord('z')+1):
    if chr(ch) not in string:
        print("string is not panagram")
        break
else:
    print("string is panagram")

