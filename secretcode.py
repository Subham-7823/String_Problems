#Write a program to analyze a string and display the count of alphabets, numbers, spaces, and special symbols.
small=0
capitals=0
num=0
special=0
space=0
str = input("Enter the string you want to check")

for i in str:
    if i.islower():
        small += 1
    elif i.isupper():
        capitals += 1
    elif i.isdigit():
        num += 1
    
    elif i.isspace():
        space += 1
    else:
        special+=1
print(f"samll {small}")
print(f"capitals {capitals}")
print(f"num {num}")
print(f"special {special}")
print(f" space {space}")
