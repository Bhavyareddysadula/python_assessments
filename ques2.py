D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3}
D_UNION = {}
for key in D1:
    D_UNION[key] = D1[key]
for key in D2:
    if key not in D_UNION:
        D_UNION[key] = D2[key]
print(D_UNION)

D_INTERSECTION = {}
for key in D1:
    if key in D2:
        D_INTERSECTION[key] = D1[key]
print(D_INTERSECTION)
    
D_DIFFERENCE = {}
for key in D1:
    if key not in D2:
        D_DIFFERENCE[key] = D1[key]
print(D_DIFFERENCE)

D_MERGE = {}
for key in D1:
    D_MERGE[key] = D1[key]
for key in D2:
    if key in D_MERGE:
        D_MERGE[key] += D2[key]
    else:
        D_MERGE[key] = D2[key]
print(D_MERGE)
