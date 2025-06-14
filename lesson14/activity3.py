outputfile=open('updated.txt','w')
inputfile=open('example.txt','r')
lines=set()
print("elimate duplicate lines")
for line in inputfile:
    if line not in lines:
        outputfile.write(line)
        lines.add(line)
inputfile.close()
outputfile.close()
