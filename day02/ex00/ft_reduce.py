from functools import reduce
import operator

def ft_reduce(function_to_apply, list_of_inputs):
    lst = list_of_inputs
    ret = lst[0]
    for i in range(1, len(lst)):
        ret = function_to_apply(ret, lst[i])
    return ret

lis = [ 1, 3, 4, 10, 4 ]

def addnb(x, y):
    return x + y
# priting summation using reduce()
print ("The summation of list using reduce is : ",end="")
print (reduce(addnb,lis))
print ("The summation of list using reduce is : ",end="")
print (ft_reduce(addnb,lis))

print ("The concatenated product is : ",end="")
print (reduce(operator.add,["coucou","ca","va"]))
print ("The concatenated product is : ",end="")
print (ft_reduce(operator.add,["coucou","ca","va"]))

print ("The maximum element of the list is : ",end="")
print (reduce(lambda a,b : a if a > b else b,lis))
print ("The maximum element of the list is : ",end="")
print (ft_reduce(lambda a,b : a if a > b else b,lis))

print ("The product of the list elements is : ",end="")
print (reduce(lambda a,b : a*b,lis))
print ("The product of the list elements is : ",end="")
print (ft_reduce(lambda a,b : a*b,lis))