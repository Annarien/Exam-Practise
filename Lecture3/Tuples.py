# Tuples are like lists except you cant change them
# defined as () where as lists are[]
#nomrally used to return values from functions


mylist=('a','b',4.0,5,['d',99])
print (mylist)
print (mylist[0])
print (mylist[1])
print (mylist[2])
print (mylist[3])
print (mylist[4])
print (mylist[-1])
print (mylist[-2])
print (mylist[-3])
print (mylist[-4])
print (mylist[-5])

mylist[0]='c' #recall: you cant change tuples ==== ERROR
print (mylist)