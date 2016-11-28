__author__='RealmL'

import random

def metrix_init(m1:list,m2:list,res:list,x:int,y:int):

    for i in range(x,y):
        temp=[]
        for j in range(x,y):
            temp.append(random.randint(0,10))
        m1.append(temp)

    for i in range(x,y):
        temp=[]
        for j in range(x,y):
            temp.append(random.randint(0,10))
        m2.append(temp)

    for i in range(x,y):
        temp=[]
        for j in range(x,y):
            temp.append(0)
        res.append(temp)

    return m1,m2,res


if __name__ =='__main__':
    m1,m2,res=metrix_init([],[],[],0,100)
    print(m1)
    print(m2)

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            a=m1[i]
            b=[row[j] for row in m2]
            sum=0
            for k in range(len(m2)):
                sum+=a[k]*b[k]
            res[i][j]=sum

    print(res)

