# new_file=open('new_file.txt','x')
# new_file.close()
import os
print('checking if the file exist or not')
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file dose not exist")
my_file=open ("my_file.txt","w")
my_file.write("hello my name is aarav")
my_file.close()
# os.remove('codingal.txt')
# os.rmdir('folder')

