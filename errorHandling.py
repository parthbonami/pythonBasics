
from wsgiref.validate import ErrorWrapper
from xml.dom.pulldom import ErrorHandler


a = [1,2,3]
tuple = tuple(a)
print(tuple)
try:
    for i in range(len(a)):
        print(a[i],end=", ")
        tuple.update(2)

    print(a[10])
except BaseException as e:
    print(e)

#Some error examples 
# 1.NameError
#2.ZeroDivisionError
#3.IOError
#4.TypeError