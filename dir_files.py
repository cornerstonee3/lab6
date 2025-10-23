import os
import string
# #task1
# put=input("enter the path:")
# print("directories:")
# print([d for d in os.listdir(put) if os.path.isdir(os.path.join(put, d))])
# print("files:")
# print([f for f in os.listdir(put) if os.path.isfile(os.path.join(put, f))])
# print("together:")
# print(os.listdir(put))
# #task2
# put=input("enter path:")
# print("exists:", os.access(put, os.F_OK))
# print("readable:", os.access(put, os.R_OK))
# print("writable:", os.access(put, os.W_OK))
# print("executable:", os.access(put, os.X_OK))
# #task3
# put=input("enter path:")
# if os.path.exists(put):
#     direc=os.path.dirname(put)
#     print("directory:", direc)
#     file=os.path.basename(put)
#     print("file name:", file)
# else:
#     print("path doesnt exist")
# #task4
# txt=input("enter file's name:")
# if os.path.exists(txt):
#     with open(txt, 'r') as f:
#         count=f.readlines()
#         print("number of lines:",len(count))
# else:
#     print("no such file")
# #task5    
# listik=["99", "mouse", "onay", "watches"]
# with open("lab6_test.txt", "w") as f:
#     for i in listik:
#         f.write(i+"\n")
# #task6
# for i in string.ascii_uppercase:
#     f=open(f"{i}.txt", "w")
#     f.close()
# #task7
# txt1=input("original file:")
# txt2=input("second file:")
# with open(txt1, "r") as f1:
#     data = f1.read()
# with open(txt2, "w") as f2:
#     f2.write(data)
#task8
put=input("etner file:")
if os.path.exists(put):
    if os.access(put, os.R_OK) and os.access(put, os.W_OK) and os.access(put, os.X_OK):
        os.remove(put)
    else:
        print("no access")
else:
    print("file doesnt exist") 
   

        