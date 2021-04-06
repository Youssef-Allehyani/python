import numpy as np

W = 5
wm = np.array([0,3,2,4,1])
vm = np.array([0,8,3,9,6])
n = len(vm)
cost = np.array([[0 for i in range(5 + 1)] for j in range(4+1)])

# def staticmethod(n,W,wm,vm):
#     for w in range(W):
#         cost[0][w] =0
#     for i in range(n):
#         cost[i][0] = 0
#     for i in range(1,n+1):
#         for w in range(1,W+1):
#             if wm[i] > w:
#                 cost[i][w] = cost[i-1][w]  
#             elif vm[i]+cost[i-1][w-wm[i]] > cost[i-1][w]:
#                 cost[i][w] = vm[i] + cost[i-1][w-wm[i]] 
#             else:
#                 cost[i][w] = cost[i-1][w]
#     print(cost)            
#     return cost[n][W]    





def knapSack(W, wt, val, n):
    K = np.array([[0 for x in range(W + 1)] for x in range(n + 1)])
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]],  
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    print(K)            
 
    return K[n][W]
 
 
# Driver code
val = np.array([8,3,9,6])
wt = np.array([3,2,4,1])
W = 5
n = len(val)
print(knapSack(W, wt, val, n))




