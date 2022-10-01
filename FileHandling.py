#File handling

#old method
from tokenize import String


#file = open('oldFile.txt','a+')
#file.write("Test data added")
#file.write("Second Line")
#for i in file:
#    print(i)
#print(file.read)

#file.close()

#new method
with open("newFile.txt","r") as file:
    #file.write("hello \n world")
    data = file.read()
    print(data)
