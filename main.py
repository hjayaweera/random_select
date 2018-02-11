import random
import numpy as np
import matplotlib.pyplot as plt

class File(object):
    file_name="test.txt"
    file_mode="r"
    def __init__(self,file_name="test.txt",file_mode="r"):
        self.file_name=file_name 
        self.file_mode=file_mode

    def read_file(self):
        if(self.file_mode=="r"):
            f = open(self.file_name,self.file_mode)
            message = f.read().split('\n')
            f.close()
        return message
    
    def append_file(self,message):
        if(self.file_mode=="a"):
            f = open(self.file_name,self.file_mode)
            f.write(message+"\n")
            f.close()

    def write_file(self,message):
        if(self.file_mode=="w"):
            f = open(self.file_name,self.file_mode)
            f.write(message)
            f.close()
        

class Rand(object):
    list_in=""
    def __init__(self,list_in):
        self.list_in=list_in
    def select_rand(self,no_of_items=1):
        #if list is short send everything available
        selected=random.choice(self.list_in)
        return selected

class select_rand(object):
    n=1
    def __init__(self):
        pass
    def select(self,list,n=1):
        self.n =n
        

f1=File("input_file.txt","r")
f2=File("output_file.txt","a");
available_list=f1.read_file()
r=Rand(available_list)
m=r.select_rand(1)
available_list.remove(m)
f2.append_file(m);
f3=File("input_file.txt","w");
list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in list1)

f3.write_file('\n'.join(available_list));

print(m)
#f2=File("output.txt","a")
#f2.append_file(f1.read_file())
#f3=File("output.txt","r")


