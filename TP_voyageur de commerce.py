import numpy as np
import random
from math import exp

x = [0,1,2,3,4,5,6,7,8,0]
x = [0,1,3,5,7,2,4,6,8,0]
x = [0,1,2,5,6,7,8,4,3,0]

V1 = 0
V2 = 0
V3 = 0

r = 0.1


# Matrice
M = [
            [0, 3, 2, 3, 4, 4, 6, 1, 7],
            [3, 0, 5, 4, 3, 6, 1, 9, 2],
            [2, 5, 0, 1, 6, 1, 9, 3, 7],
            [3, 4, 1, 0, 5, 9, 7, 2, 1],
            [4, 3, 6, 5, 0, 9, 1, 2, 1],
            [4, 6, 1, 9, 9, 0, 2, 1, 7],
            [6, 1, 9, 7, 1, 2, 0, 4, 5],
            [1, 9, 3, 2, 2, 1, 4, 0, 7],
            [7, 2, 7, 1, 1, 7, 5, 7, 0]
    
    ]

print(M)

def dist(x):
    distx = 0
    for i in range(9):
        distx = distx + M[x[i]][x[i+1]]
    return distx

xx = [1,2,3,4,5,6,7,8]
xx1 = xx[:]
random.shuffle(xx1)
x1 = [0]+xx1+[0]
xx1 = xx[:]
random.shuffle(xx1)
x2 = [0]+ xx1+[0]
xx1 = xx[:]
random.shuffle(xx1)
x3 = [0]+ xx1+[0]
xx1 = xx[:]
random.shuffle(xx1)
x4 = [0]+ xx1+[0]
xx1 = xx[:]
random.shuffle(xx1)
x5 = [0]+ xx1+[0]
xx1 = xx[:]
random.shuffle(xx1)
x6 = [0]+ xx1+[0]

T = 0
xy = [1,2,3,6]

def croisement(vect,vect1,vect2):
    l2 =2
    l4 =6
    l6 = 8

    i=1
    while i <= l2:
        vect[i]=vect1[i]
        i=i+1
    
    while i<=l4:
        if vect2[i] not in vect:
            vect[i]=vect2[i]
        i=i+1
    while i<=l6:
        if vect1[i] not in vect:
            vect[i]=vect1[i]
        i=i+1
    k=1
    while k<9:
        if k not in vect:
            i=1
            while i <9:
                if vect[i]<0:
                    vect[i]=k
                    i=8
                i=i+1
        k=k+1
    return vect

def croisement2(vect,vect1,vect2):
    l2 =2
    l4 =6
    l6 = 8

    i=1
    while i <= l2:
        vect[i]=vect1[i]
        i=i+1
    
    while i<=l4:
        if vect2[i] not in vect:
            vect[i]=vect2[i]
        i=i+1
    while i<=l6:
        if vect1[i] not in vect:
            vect[i]=vect1[i]
        i=i+1
    k=1
    while k<9:
        if k not in vect:
            i=1
            while i <9:
                if vect[i]<0:
                    vect[i]=k
                    i=8
                i=i+1
        k=k+1
    return vect
courbe = []


while T < 500:
    x7 = [0,-1,-1,-1,-1,-1,-1,-1,-1,0]
    x7 = croisement2(x7,x1,x2)
    
    x8 = [0,-1,-1,-1,-1,-1,-1,-1,-1,0]
    x8 = croisement2(x8,x3,x4)
    
    x9 = [0,-1,-1,-1,-1,-1,-1,-1,-1,0]
    x9 = croisement2(x9,x5,x6)
    
    x10 = [0,-1,-1,-1,-1,-1,-1,-1,-1,0]
    x10 = croisement2(x10,x2,x1)
    
    x11 = [0,-1,-1,-1,-1,-1,-1,-1,-1,0]
    x11 = croisement2(x11,x4,x3)
    
    x12 = [0,-1,-1,-1,-1,-1,-1,-1,-1,0]
    x12 = croisement2(x12,x6,x5)
    
    r1 = random.randint(1,8)
    r2 = random.randint(1,8)
    
    while r1==r2:
        r1 = random.randint(1,8)
        r2 = random.randint(1,8)
    temp = x7[r1]
    x7[r1] = x7[r2]
    x7[r2] = temp
    
    r1 = random.randint(1,8)
    r2 = random.randint(1,8)
    
    while r1==r2:
        r1 = random.randint(1,8)
        r2 = random.randint(1,8)
        
    temp = x9[r1]
    x9[r1] = x9[r2]
    x9[r2] = temp
    
    r1 = random.randint(1,8)
    r2 = random.randint(1,8)
    
    while r1==r2:
        r1 = random.randint(1,8)
        r2 = random.randint(1,8)
        
    temp = x11[r1]
    x11[r1] = x11[r2]
    x11[r2] = temp
    
    r1 = random.randint(1,8)
    r2 = random.randint(1,8)
    
    
distx = [0,0,0,0,0,0,0,0,0,0,0,0]    
distx[0] = dist(x1)
distx[1] = dist(x2)
distx[2] = dist(x3)
distx[3] = dist(x4)
distx[4] = dist(x5)
distx[5] = dist(x6)
distx[6] = dist(x7)
distx[7] = dist(x8)
distx[8] = dist(x9)
distx[9] = dist(x10)
distx[10] = dist(x11)
distx[11] = dist(x12)

TR = [1,2,3,4,5,6,7,8,9,10,11,12]
t= 0
dst = distx[:]

while t <12:
    b = t+1
    while b <12:
        if distx[b] < distx[t]:
            temp = TR[t]
            TR[t] = TR[b]
            TR[b] = temp
            temp = distx[t]
            distx[t] = distx[b]
            distx[b] = temp
        b = b+1
    t = t+1
M1 = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]

courbe = courbe + [distx[0]]
    
MM = [
    M1[TR[0]-1][:],
    M1[TR[1]-1][:],
    M1[TR[2]-1][:],
    M1[TR[3]-1][:],
    M1[TR[4]-1][:],
    M1[TR[5]-1][:],
    M1[TR[6]-1][:],
    M1[TR[7]-1][:],
    M1[TR[8]-1][:],
    M1[TR[9]-1][:],
    M1[TR[10]-1][:],
    M1[TR[11]-1][:]   
]

l3 = 3
l4 = 11
l1 = 0
l2=2
c1 = random.randint(l3,l4)
c2 = random.randint(l3,l4)
while c1 == c2:
    c1 = random.randint(l3,l4)
    c2 = random.randint(l3,l4)
c3 = random.randint(l3,l4)
while c3 == c2 or c3 == c1:
    c3 = random.randint(l3,l4)

a1 = random.randint(l1,l2)
a2 = random.randint(l1,l2)

while a1 == a2:
    a1 = random.randint(l1,l2)
    a2 = random.randint(l1,l2)
a3 = random.randint(l1,l2)
while a3 == a2 or a3 == a1:
    a3 = random.randint(l1,l2)

print('x1 =', x1, "dist=", dist[0])
x1 = MM[a1][:]
T = T+1