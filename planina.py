#! /usr/bin/python3
N = int(input().strip())    
def svar(N):
    temp1 = 4**N
    temp2 = (2**(N+1))+1
    ans = temp1 + temp2
    return ans
print(svar(N))
