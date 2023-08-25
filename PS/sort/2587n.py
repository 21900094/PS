import numpy as np

n_list=list()
for i in range(0,5):
    a=int(input())
    n_list.append(a)
mean=np.mean(n_list)
median=np.median(n_list)
mean=int(mean)
median=int(median)
print(mean)
print(median)