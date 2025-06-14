with open('example.txt') as fp:
    data1=fp.read()
with open('my_file.txt') as fp:
    data2=fp.read()
data1=data1+"\n"
data2=data2+"\n"
print("merging two files")
with open ('mergedfile.txt','w') as fp:
    fp.write(data1)