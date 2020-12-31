import os
import json
import time
from sys import getsizeof
from Packages import ttldict
gb=1073741824
kb=16000

def ifFileExistes(FileName):
    return os.path.exists(FileName)
    
def create(dic,fi):
        size = os.path.getsize(fi)/gb
        if size<1:
            n=int(input("Enter number of key value pairs :"))
            count=0
            while count<n:
                    k=input("Enter the key: ")
                    if len(k)<32:
                        if k not in dic:
                                v=input("Enter the value:")
                                if (getsizeof(v)/kb)<16:
                                    dic[k]=v
                                    dic[k]=ttldict.TTLDict(ttl=2)
                                    count+=1
                                else:
                                    print("Size of value exceeds 16 KB,cannot insert the key value pair")
                        else:
                                print("key already exists")
                    else:
                        print("Length of key should be at most 32")
        else:
            print("The file size exceeds 1GB cannot create")

def delete(dic):
        if len(dic)>0:
                k=input("Enter the key to be deleted: ")
                if k in dic:
                    if len(dic[k])==0:
                        print("Key-Value pair expired")
                    else:
                        del dic[k]
                else:
                        print("No key value pair exist")
        else:
                print("Json file is empty")

def read(dic):
        if len(dic)>0:
                k=input("Enter the key: ")
                if k in dic:
                    if len(dic[k])==0:
                        print("Key-Value pair expired")
                    else:
                        print(f'The value for {k} is {dic[k]}')          
                else:
                        print("No key value pair exist")
        else:
                print("Json file is empty")

def display(dic,fi):
    print("Choose from the given option")
    print("1.Create")
    print("2.Read")
    print("3.Delete")
    print("4.Exit")
    k=input("Enter Your option ")
    if k=='1':
        create(dic,fi)
        display(dic,fi)
    elif k=='2':
        read(dic)
        display(dic,fi)
    elif k=='3':
        delete(dic)
        display(dic,fi)
    elif k=='4':
        with open(fi,'w') as f:
            json.dump(dic,f,indent=2)       
    else:
        print("Enter a Valid option ")
        display(dic)

def main():
    check=input("Do You want to open an existing JSON file? If yes press Y , else press N \n")
    if check == 'Y' or check=='y':

        FileName=input("Enter the JSON file name\n")
        FileName=FileName+'.json'
        flag=ifFileExistes(FileName)

        if flag==True:
            fi=os.getcwd()+"\\"+FileName
            if os.path.exists(fi):
                size = os.path.getsize(fi)/gb
                if size<1:
                    try:
                        os.rename(fi, fi)
                        with open(FileName) as f:
                            dic=json.load(f)
                        display(dic,FileName)
                    except OSError as e:
                        print("File is currently being used by another process")
                else:
                    print("The file you are trying to open is more than 1 GB,cannot open")
            
        else:
            dic={}
            display(dic,FileName)
    else:
        dic={}
        FileName=input("Enter the file name to save\n")
        FileName=FileName+'.json'
        display(dic,FileName)

        
