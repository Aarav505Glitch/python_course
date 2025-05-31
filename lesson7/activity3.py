def test(lst):
    result={}
    for item in lst: 
        result[item[0]]=item[1:]
    return result
students=[[1,"jon","V"],[2,"brian","VII"],[3,"aarav","XI"]]
print("\n original list")
print(students)
print("\n coverted list")
print(test(students))