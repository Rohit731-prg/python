# Get the Class Name of an Instance

class myClass1:
    pass

class myClass2:
    pass

fun1 = myClass1()
fun2 = myClass2()

name1 = fun1.__class__.__name__
name2 = fun2.__class__.__name__

print("First Class Name : ", name1)
print("Second Class Name : ", name2)