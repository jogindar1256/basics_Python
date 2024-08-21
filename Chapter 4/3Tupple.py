a = ("Jogindar", "list", False, 56, 44, 324, "Qbola", 44)


# counting the number of data
no = a.count(44)
print(no)

# finding the index number of the element
i = a.index(56)
print(i)

#Membership in the tupple check by `in` keyword
print(44 in a)   #Returns True or False


#Check the length of the tupple
print(len(a))


#Unpacking the tupple: can print it into each value in different var
b, c, d, e, f, g, h, j = a
print(b, c, d, e, f, g, h, j)