def addthis(x,y):
    print(f"this is x {x} and the type is {type(x)} this is y{y} and the type is {type(y)}")
    
    try:
        result= x+y
    except TypeError:
        print(f"Thr wrong type passed")\
            
    print(f"This is the result {result}")
    return result

print(addthis(1,2))