def add(x,y):
    return x+y

def conc(x,y):
    return str(x)+str(y)

def operate(operation,x,y):
    return operation(x,y)

result=operate(add,3,5)
print("Result of sum:",result)
result_2=operate(conc,"Hello","World");
print("Result is:",result_2)