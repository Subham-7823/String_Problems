#write a program that will print the following sqequence
input = "hello i am going"
output = ["going","am","i","hello"]

L=[]
word=""

for ch in input:
    if ch==" ":
        L = [word] + L 
        word=""
    else:
        word+=ch
L=[word]+L
print(L)
