import itertools

a = int(input())
strspis = []
for i in range(a):
    b = int(input())
    spis = []
    for i in range(b):
        spis.append(input())
    chisl = ['0','1','2','3','4','5','6','7','8','9']
    str = ''
    for subset in itertools.permutations(spis, 3):
        flag1 = 0
        for element in chisl:
            flag = 0 
            for element1 in subset:
                if(element in element1):
                    flag +=1 
            if(flag > 0 ):
                flag1 +=1
        if(flag1 == 10):
            str = subset[0] + ' ' + subset[1] + ' ' + subset[2]
            break
    strspis.append(str)
for element in strspis:
    print(element)
