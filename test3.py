import numpy as np

a = [1, 4, 8, 9, 10, 11, 12, 13, 17, 23, 24, 25, 26, 27, 42, 55, 56, 57,58]
B = [0, 1, 2, 3, 4, 5, 6, 7]
C = [2, 4, 8]

#print(B[1:9])
#print(a[2:8], a[9:14], a[15:18])
print(B[0:8])
def modify_order(a):
    lis = []
    d = -1
    e = 0
    k = 1
    for i, val in enumerate(a):
        if i != (len(a)-1):
            if val == a[i+1] - 1:
                if d == -1 and lis == []:
                    d = i
                    print(d,i, "dddd")
                if d == -1 and lis != []:
                    d = i
                e = d + k
                k += 1
            else:
                if d != -1 and e != 0:
                    lis.append(d)
                    lis.append(e+1)
                    d=-1
                    e=0
                    k=1

        if i == len(a)-1 and d != -1:
            e = d + k
            lis.append(d)
            lis.append(e)
    lis = np.array(lis)
    lis = np.split(lis,len(lis)/2)
    return lis[0]

print(modify_order(a))