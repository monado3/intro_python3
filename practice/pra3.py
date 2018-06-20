lis0=[0,1,2]
print(lis0[0:2])
print(type(lis0[0]))

print(lis0[::2])

print(lis0[::-2])

print(lis0[::-1])

lis1=[3,4]
lis0.extend(lis1)
print(lis0)

lis0.insert(2,1.5)
print(lis0)

del lis0[2]
print(lis0)

lis0.remove(3)
print(lis0)

print(lis0.pop(1))
print(lis0)

print(2 in lis0)

print(lis0.count(2))
print(lis0.count(1))

print(len(lis0))

a=[1,2,3]

empty_tuple=()

abc_tuple=(1,2,3)
a,b,c=abc_tuple
print(a,b,c)

abc_dic={'a':1,'b':2}
defg_dic={'d':4}
abc_dic.update(defg_dic)
print(abc_dic)

print('a' in abc_dic)

print(abc_dic['a'])

print(abc_dic.get('c','Not in dic'))

a={1,2}
b={2,3}

print(a&b)
print(a.intersection(b))

print(a|b)
print(a.union(b))

print(a-b)
print(a.difference(b))

print(a^b)
print(a.symmetric_difference(b))

print(a<=b)
print(a.issubset(b))
