from copy import deepcopy


list = list()
list.append(1)
list.append(2)
print(list)
print(len(list))
list2 = list # shallowCopy
print("Before changes: ")
print("list :", list)
print("list2 :",list2)
list.append(3)
list2.append(4)
print("After Changes:")
print("list :", list)
print("list2 :",list2)
list3 = list.copy()
list3.append(5)
print("After Changes:")
print("list :", list)
print("list2 :",list2)
print("list3 :",list3)
list4 = deepcopy(list) # deepcopy
list4.append(6)
print("After Changes:")
print("list :", list)
print("list2 :",list2)
print("list3 :",list3)
print("list4 :",list4)