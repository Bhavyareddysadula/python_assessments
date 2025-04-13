"""convert(x)          Converts like below 
                    input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
                    output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]"""



def convert(x):
    output = []
    for i in x:
        temp1 = []
        for j in i:
            temp2 = []
            for k in j:
                lst = k.replace('(', '').replace(')', '')
                new_lst = lst.split(',')
                temp3 = []
                for n in new_lst:
                    temp3.append(int(n))
                temp2.append(temp3)
            temp1.append(temp2)
        output.append(temp1)
    return output

print(convert([[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]))
    
