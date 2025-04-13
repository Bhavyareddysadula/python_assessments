"""flatten(lst)        Flattens the list 
                    ie input = [1,2,3, [1,2,3,[3,4],2]]
                    output = [1,2,3,1,2,3,3,4,2]"""


def flatten(lst):
    result = []
    for e in lst:
        if type(e) == list:
            flattened = flatten(e)
            for i in flattened:
                result.append(i)
        else:
            result.append(e)
    return result
print(flatten([1,2,3, [1,2,3,[3,4],2]]))


            
    
