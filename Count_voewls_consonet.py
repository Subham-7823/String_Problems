#write a program that will count voewls and consonets from the string
string = "areuuieqrwecwWW"
vowels=""
consonent=""
for ch in string:
    if ch in 'aeiouAEIOU':
       vowels = vowels + ch
    else:
        consonent = consonent + ch
print("Vowel are :",vowels)
print("Consonets are :",consonent)
