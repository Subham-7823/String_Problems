#write a program that will tell given string is anagram or not 

#LOGIC
# if we rearrange the given string
# 1.The generated string must be same length
# 2.The genarated string must consist same elements
# 3.The genearted string must have same repetation of elemnts

# EXAMPLE
# "rome"
# rearrange
# "more"
# "reom"
s1="rome"
s2="more"
if len(s1)==len(s2):
    for ch in s1:
        if (ch not in s2) or (s1.count(ch)!=s2.count(ch)):
            print("String in not Anagram")
            break
    else:
        print("String is Anagram")
else:
    print("String is not Anagram")