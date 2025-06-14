with open('example.txt','w' ) as file:
    file.write("hello i am aarav my age is 15")
file.close()
with open('example.txt','r') as file:
    data=file.readlines()
    print("words in the file are ")
    for line in data :
        word=line.split()
        print(word)
file.close()