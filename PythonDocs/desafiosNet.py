l = list("1234")
l[0] = l[1] = 5
print(l)

#----------------------------

a = [2]
a.append(a.append(3))
print(a)

#----------------------------

a = {2, 3, 4}
a.remove(2)
a.add(5)
print(a)

#---------------------------

x = "abcdef"
i = "a"
while i in x:
    print(i, end = " ")