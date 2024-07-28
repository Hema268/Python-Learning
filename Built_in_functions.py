#Built in function

#abs() returns absolute value
print("1. ",abs(-3.44))
print("2. ",abs(3+5j))
#all() If the iterable object is empty, the all() function also returns True.
mylist = []
print("3. ",all(mylist))

#any() returns true if any item is iterable
c = [False, 1, False]
print("4. ",any(c))

#bin()
print("5. " ,bin(18)[-8:])

#compile
d = compile('print(55)', 'test', 'eval')
exec(d)

#dict() function creates a dictionary
print("7. ",dict(name = "John", age = 36, country = "Norway"))

#divmod()
print("8. ",divmod(5, 2))

#enumerate()
e = ('Python', 'c', 'html','css')
print("9. [dictionary]",dict(enumerate(e)))
print("  => [list]",list(enumerate(e)))
print("  => [tuple]",tuple(enumerate(e)))
print("  => [set]",set(enumerate(e)))

#eval()
eval('print(55+44)')

#filter()
#filter() function returns an iterator where the items are filtered through a function to testif the item is accepted or not.
print("11. filter()")
age = [5,6,20,18,45,33]
def func(x):
    if x < 18:
        return False
    else:
        return True
for x in filter(func,age):
    print(x)

#format()
print("12. " ,format(255,'X'))
