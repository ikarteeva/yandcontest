a = int(input())
if(a>1000000):
    print(0)
else:
    c = int(input())
    if(c==a):
        print(0)
    else:
        ver = []
        var = []
        for i in range(a):
            b = float(input())
            var.append(b)
        j=0


        sumout = []
        for element in var:
            k=j

            if(j+c<len(var)+1):
                nnd=[]
                for i in range(c):
                    nnd.append(k)
                    k+=1
            prh = 0
            sum = 0
            for element1 in var:
                if(prh not in nnd):
                    sum = sum + element1
                prh += 1
            sumout.append(sum)
            j+=1
        print(min(sumout))
