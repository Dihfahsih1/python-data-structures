l =[1,2,3,4,5]
m = map(lambda x: 2**x, l)
print(list(m))

array = ["welcome","To", "Turing"]
print("-".join(array))

def listSkill(val, list=[]):
  list.append(val)
  return list
list1 = listSkill('Nodejs' )
list2 = listSkill('Java')
list3 = listSkill('Reactjs',[])

print("%s" % list1)
print("%s" % list2)
print("%s" % list3)