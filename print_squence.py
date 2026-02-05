#write a program thta will print following sequence
input = "abcd hello hi bye"
output =["dcba","olleh","ih","eyb"]

l=[]
word=""
for ch in input:
    if ch ==  " ":
        l=l+[word]
        word=""
    else:
        word = ch + word 
l=l+[word]
print(l)