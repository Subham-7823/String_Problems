#write a program that will print words from string and 
#that words are  from string
input = "er iqeur qurtupq"
output = ["er","iqeur","qurtupq"]

l=[]
word=""
for ch in input:
    if ch==" ":
        l=l+[word]
        word=""
    else:
        word+=ch
l=l+[word]
print(l)