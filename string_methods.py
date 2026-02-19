

#string methods
a="subham"
print(len(a))  #5

#converting to uppercase
# when we perform some operation on string we get a new string
print(a.upper()) #SUBHAM
print(a) #subham

#convering to lowercase
print(a.lower())   #subham


#removeing trailing charecter
b="Harry!!!!!!"
print(b.rstrip("!"))  #Harry


#replace()
#it replaces all the matching charecters with given charecters
print(b.replace('r','e')) #Haeey!!!!!!


#split()
# split() is a string method used to break a string into parts based on a separator and return them as a list
#it splits the string with respect to given charecter
#output comes in form list
c="subham jyoti rana"
print(c.split(" "))
#we are spliting with respect to single space
# ['subham', 'jyoti', 'rana']


#if we dont pass any value in split method it splits the string with one space by defalut


#capitialize()
#it capitilize the first charecter of string
print(c.capitalize())
#Subham jyoti rana
#it capitalize only the first charecter of string





#center()
d="hello"
print(d.center(10)) #     hello
print(len(d))#5
print(len(d.center(10)))#10
#it will give given no space in string
#given 10 and srtring length is 5
#so center() gives my space before string
#so that the total length of string became 10



#count()
#count method is used give occurance of a chrecter in string
print(d.count('l'))#2



#endswith()
#it checks string is ends with the particular cahrecter or not
e="Hello WOrld !!!"
print(e.endswith("!"))#True
#it will print result in boolean

#we can also check particular part of string also
f="Hello this is subham"
print(f.endswith('is',1,13))#True
#like sliceing



#find()
#it is used to give the first given charecter occurance in string
g="He is a good boy but he is not selfish"
print(g.find("is"))#3
#it will print first occured index position of charecter in string

#if given charecter is not present in string it will return -1
print(g.find("wer"))#-1




#index()
#index method is also same as find
#but where find() return -1 when it does not find the charecter
#but index() returns error if it does not find the charecter in string
#print(g.index("wer"))
#op
#Traceback (most recent call last):
#  File "<main.py>", line 88, in <module>
#ValueError: substring not found


#isalnum()
#it is used to check your string is alphanumeric 
h="dtring#$"
print(h.isalnum()) #False



#isapha
#in isalph numbers and special charecters not comes .
#it gives true when present charecter between a-z and A-Z
print(h.isalpha()) #False
i="asdAS"
print(i.isalpha()) #True



#isprintable()
#it returns true when printable charecter is present in the string
print(i.isprintable()) #True
i="adjnwej\n"
print(i.isprintable()) #False6


# istitle()
#it returns true if the first letter of the word is capital
print(i.istitle()) #False


#startswith()
#it returns true when string is strarts with given charecter
print(i.startswith("a"))  #True

