__author__='RealmL'

import random
from _thread import start_new_thread

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


def multiTwoLine(l1: list, l2: list, res: list, i: int):
    #每个线程需要执行的函数
    for j in range(len(l2[0])):
        a = l1[i]
        b = [row[j] for row in l2]
        sum = 0
        for k in range(len(m2)):
            sum += a[k] * b[k]
        res[i][j] = sum


if __name__ =='__main__':
    m1,m2,res=metrix_init([],[],[],0,1000)
    print(len(m1))
    print(len(m2))

    #单线程
    # for i in range(len(m1)):
    #     for j in range(len(m2[0])):
    #         a=m1[i]
    #         b=[row[j] for row in m2]
    #         sum=0
    #         for k in range(len(m2)):
    #             sum+=a[k]*b[k]
    #         res[i][j]=sum
    #
    # print(len(res))

    #多线程
    for i in range(len(m1)):
        start_new_thread(multiTwoLine,(m1,m2,res,i))

    print(len(res))


    # multiTwoLine(m1,m2,res,0)

    print(res[0][0])
