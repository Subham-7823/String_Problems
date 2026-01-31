#write a pyhton program that will count occurance of charecter 
string = "ennnngineering"
res=""
for ch in string:
    if ch not in res:
        res+=ch
for new_chr in res:
    print(new_chr," ",string.count(new_chr))