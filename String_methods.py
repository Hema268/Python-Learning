# String Methods 
# split()
txt = "welcome to the jungle"
print(txt.split(" "))
# strip() "Removes unwanted spaces"
x = "      i am hema"
print(x.strip())
#join
myTuple = ("John", "Peter", "Vicky")
print("_-_".join(myTuple))
#centre()
y = "banana"
print(y.center(20,"-"))
#expendtabs
txt = "My\tname is \tStale"
x =  txt.expandtabs(8)
print(x)
#formatting
print("My name is {}, I'm {}".format("John",36))
print("My name is {n} , I'm {a}".format(n = "Hema",a = 20 ))
print("{1} {0} {3} {3:b}".format(1,2,3,4))

# isdigit
n = "10122933"
print(n.isdigit())
#zfill 
tx = "50"
print(tx.zfill(10))
