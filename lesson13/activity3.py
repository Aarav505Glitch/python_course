file1=open('codingal.txt','r')
file2=open('codingal_update.txt','w')
for line in file1.readlines():
    if( line.startswith ('Coding')):
        print(line)
        file2.write(line)
file2.close()
file1.close()