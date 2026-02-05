#write a program that will only print numbers from string without using builtin methods and
#use while loop
string = "asrkabk34kjjnalal76tr8945$#$%#$"
res="" 
count=0
while count < len(string):
    if  "0" <= string[count] <= "9":
        res+=string[count]
    count=count+1
print(res)

